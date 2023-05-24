#!/usr/bin/env nextflow
nextflow.enable.dsl=2

params.input_merge = "$baseDir/data/*.mzML"

TOOL_FOLDER = "$baseDir/bin"
OUTPUT_FOLDER = "$baseDir/nf_output"
DATA_FOLDER = "$baseDir/data"

process createIndividualHistogram {
    publishDir "$DATA_FOLDER", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    file input

    output:
    file "*.pickle"

    """
    massql ${input} "QUERY scaninfo(MS2DATA)"
    python $TOOL_FOLDER/create_individual_histogram.py ${input.baseName}.mzML_ms2.msql.feather ${input}.pickle
    rm *feather
    """
}


process mergeData {
    publishDir "./nf_output", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    file "individual/*"

    output:
    file "mergedset_${task.index}.pickle"

    script:
    """
    python $TOOL_FOLDER/mergedata.py individual mergedset_${task.index}.pickle

    """
}

process createHist {
    publishDir "./nf_output", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    file "merged/*"

    output:
    file "finalhist.png"

    script:
    """
    python $TOOL_FOLDER/createhist.py merged finalhist.png

    """
}

workflow {
    data = Channel.fromPath(params.input_merge, checkIfExists:true)

    individual_histogram_ch = createIndividualHistogram(data)
    merged_histogram_ch = mergeData(individual_histogram_ch.collate(1000))
    createHist(merged_histogram_ch.collate(1000))
}