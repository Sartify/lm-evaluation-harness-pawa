# model_name="outputs/test_output"
model_name="google/gemma-3-4b-pt"
export TRANSFORMERS_VERBOSITY=error # Suppress warnings

CUDA_VISIBLE_DEVICES=0,1 python -m lm_eval --model hf \
	--model_args pretrained=$model_name,device_map=auto \
	\
	--tasks afrimmlu_direct_zul_prompt_1,afrimmlu_translate_zul_prompt_1 \
	--batch_size 8 \
	--output_path outputs/results_pawa_mmlu.json # --tasks afrimmlu_tasks,afrimgsm_tasks,afrixnli_tasks \
