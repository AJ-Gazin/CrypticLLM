python ./utils/run_seq2seq_qa.py \
--model_name_or_path google-t5/t5-small \ 
--train_file C:\Users\aj\Code\Cryptic_project\data\clues_train.csv \ 
--validation_file C:\Users\aj\Code\Cryptic_project\data\clues_valid.csv \ 
--test_file C:\Users\aj\Code\Cryptic_project\data\clues_test.csv \
--question_column question \
--context_column context \  
--answer_column answers \ 
--do_train \ 
--do_eval \ 
--do_pred \ 
--predict_with_generate \   
--version_2_with_negative \ 
--per_device_train_batch_size 192 \ 
--learning_rate 2e-3 \  
--num_train_epochs 25 \        
--max_seq_length 64 \   
--overwrite_output_dir true \    
--output_dir C:\Users\aj\Code\Cryptic_project\