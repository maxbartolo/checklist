# Running CheckList for RC

1. Get model predictions on `squad_ans.json` using something like:

```
python transformers/examples/question-answering/run_squad_max.py   --model_type roberta   --model_name_or_path roberta-large   --do_eval   --do_lower_case   --output_dir /checkpoint/maxbartolo/qa/roberta_round1_1   --train_file None   --predict_files ~/_code/checklist/release_data/squad/squad_ans.json   --max_seq_length 512   --max_answer_length 30   --doc_stride 128   --per_gpu_eval_batch_size=128   --fp16   --null_score_diff_threshold 0.0   --max_query_length 64   --n_best_size 1   --save_predictions_to_predict_file_dir   --seed 27
```

2. `cd ~/_code/checklist`

3. Flatten model predictions using:
```
python flatten_squad_predictions.py '/private/home/maxbartolo/_code/checklist_max/predictions_bert_round2.json'
```

4. Get checklist results using:
```
python run_squad.py '/private/home/maxbartolo/_code/checklist_max/predictions_roberta_round2_1_flat.txt' > results_roberta_round2.txt
```

5. Extract result summary:
```
python extract_results_from_checklist_summary.py '/private/home/maxbartolo/_code/checklist_max/results_roberta_round2.txt'
```
