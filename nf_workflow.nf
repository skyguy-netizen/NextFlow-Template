#!/usr/bin/env nextflow
nextflow.enable.dsl=2

params.input_merge = "$baseDir/data/*.mzML"

TOOL_FOLDER = "$baseDir/bin"
OUTPUT_FOLDER = "$baseDir/nf_output"
DATA_FOLDER = "$baseDir/data"

process convertFile {
    publishDir "$DATA_FOLDER", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    file input

    output:

    file "${input.baseName}.mzML_ms2.msql.feather"

    """
    massql ${input} "QUERY scaninfo(MS2DATA)"
    """
}

process processData {
    publishDir "./nf_output", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    path input

    output:
    file "*.pickle"

    script:
    """
    python $TOOL_FOLDER/script.py $input ${input}.pickle
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
    python $TOOL_FOLDER/mergedata.py mergedset_${task.index}.pickle ${ready.size()} ${ready.join(' ')}

    """
}

process createHist {
    publishDir "./nf_output", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    val ready
    path fq

    output:
    file "finalhist.png"

    script:
    """
    python $TOOL_FOLDER/createhist.py finalhist.png ${ready.size()} ${ready.join(' ')}

    """
}

workflow {
    data = Channel.fromPath(params.input_merge, checkIfExists:true)
    converted_file_ch = convertFile(data)
    processData(converted_file_ch)
    mergeData(processData.out.collate(1000), data)
    createHist(mergeData.out.collate(1000), data)
}