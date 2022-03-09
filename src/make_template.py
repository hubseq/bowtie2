import json
MODULE = 'bowtie2'

mi_template_json = {'module_version': '00.00.00', 'program_name': 'bowtie2', 'program_subname': '', 'program_version': '2.3.5.1', 'compute': {'environment': 'aws', 'language': 'Python', 'language_version': '3.7', 'vcpus': 2, 'memory': 20000}, 'program_arguments': '', 'program_input': [{'input_type': 'file', 'input_file_type': 'FASTQ', 'input_position': -2, 'input_prefix': '-U'}, {'input_type': 'file_double', 'input_file_type': 'FASTQ', 'input_position': -2, 'input_prefix': '-1,-2'}, {'input_type': 'file', 'input_file_type': 'FASTQ.GZ', 'input_position': -2, 'input_prefix': ''}], 'program_output': [{'output_type': 'file', 'output_file_type': 'SAM', 'output_position': -1, 'output_prefix': '-S'}, {'output_type': 'file', 'output_file_type': 'BAM', 'output_position': -1, 'output_prefix': '-b'}], 'alternate_inputs': [{'input_type': 'folder', 'input_file_type': 'FASTA', 'input_position': 0, 'input_prefix': '-x'}], 'alternate_outputs': [], 'defaults': {'alternate_inputs': ['s3://npipublicinternal/test/genomes/mm10/bowtie2index/mm10.fasta'], 'output_file': '<SAMPLE_ID>.bowtie2.sam'}}
with open(MODULE+'.template.json','w') as fout:
    json.dump(mi_template_json, fout)

io_json = {'input': ['s3://npipublicinternal/test/chipseq/run_test1/fastq/mouse_control_chipseq_rep1.fastq.gz'], 'output': ['s3://npipublicinternal/test/chipseq/run_test1/bowtie2/mouse_control_chipseq_rep1.bowtie2.sam'], 'alternate_inputs': ['s3://npipublicinternal/test/genomes/mm10/bowtie2index/mm10.fasta'], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test'}
with open(MODULE+'.test.io.json','w') as fout:
    json.dump(io_json, fout)

io_json2 = {'input': ['s3://npipublicinternal/test/chipseq/run_test1/fastq/mouse_control_chipseq_rep2.fastq.gz'], 'output': ['s3://npipublicinternal/test/chipseq/run_test1/bowtie2/mouse_control_chipseq_rep2.bowtie2.sam'], 'alternate_inputs': ['s3://npipublicinternal/test/genomes/mm10/bowtie2index/mm10.fasta'], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test'}
with open(MODULE+'.test2.io.json','w') as fout:
    json.dump(io_json2, fout)

io_json3 = {'input': ['s3://npipublicinternal/test/chipseq/run_test1/fastq/mouse_heart_H3K4me3_rep1.fastq.gz'], 'output': ['s3://npipublicinternal/test/chipseq/run_test1/bowtie2/mouse_heart_H3K4me3_rep1.bowtie2.sam'], 'alternate_inputs': ['s3://npipublicinternal/test/genomes/mm10/bowtie2index/mm10.fasta'], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test'}
with open(MODULE+'.test3.io.json','w') as fout:
    json.dump(io_json3, fout)

io_json4 = {'input': ['s3://npipublicinternal/test/chipseq/run_test1/fastq/mouse_heart_H3K4me3_rep2.fastq.gz'], 'output': ['s3://npipublicinternal/test/chipseq/run_test1/bowtie2/mouse_heart_H3K4me3_rep1.bowtie2.sam'], 'alternate_inputs': ['s3://npipublicinternal/test/genomes/mm10/bowtie2index/mm10.fasta'], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test'}
with open(MODULE+'.test4.io.json','w') as fout:
    json.dump(io_json4, fout)    
    
io_dryrun_json = io_json
io_dryrun_json['dryrun'] = ''
with open(MODULE+'.dryrun_test.io.json','w') as fout:
    json.dump(io_dryrun_json, fout)

io_dryrun_local_json = {'input': ['/Users/jerry/icloud/Documents/hubseq/bowtie2/test/mouse_control_chipseq_rep1.fastq.gz'], 'output': ['/Users/jerry/icloud/Documents/hubseq/bowtie2/test/mouse_control_chipseq_rep1.bowtie2.sam'], 'alternate_inputs': ['/Users/jerry/icloud/Documents/hubseq/genomes/mm10/bowtie2index/mm10.fasta'], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test', 'dryrun': ''}

with open(MODULE+'.dryrun_local_test.io.json','w') as fout:
    json.dump(io_dryrun_local_json, fout)

# job info test JSONs
job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://npipublicinternal/test/modules/"+MODULE+"/job/"+MODULE+".test.job.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test.job.json','w') as fout:
    json.dump(io_json, fout)

job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://npipublicinternal/test/modules/"+MODULE+"/job/"+MODULE+".test.job.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test2.job.json','w') as fout:
    json.dump(io_json2, fout)

job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://npipublicinternal/test/modules/"+MODULE+"/job/"+MODULE+".test.job.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test3.job.json','w') as fout:
    json.dump(io_json3, fout)

job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://npipublicinternal/test/modules/"+MODULE+"/job/"+MODULE+".test.job.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test4.job.json','w') as fout:
    json.dump(io_json4, fout)    
