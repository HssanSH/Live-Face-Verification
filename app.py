{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3aee4f63",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-20 14:52:02.714 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-20 14:52:03.578 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Hassan Shoaib\\myenv\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-04-20 14:52:03.579 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-20 14:52:03.580 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-20 14:52:04.088 Thread 'Thread-3': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-20 14:52:04.093 Thread 'Thread-3': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\Hassan Shoaib\\myenv\\Lib\\site-packages\\keras\\src\\backend\\tensorflow\\core.py:219: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-20 14:52:04.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-20 14:52:04.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "NotImplementedError",
     "evalue": "Exception encountered when calling Layer.call().\n\n\u001b[1mCould not automatically infer the output shape / dtype of 'l1_dist_17' (of type Layer). Either the `Layer.call()` method is incorrect, or you need to implement the `Layer.compute_output_spec() / compute_output_shape()` method. Error encountered:\n\nLayer Layer does not have a `call` method implemented.\u001b[0m\n\nArguments received by Layer.call():\n  • args=('<KerasTensor shape=(None, 4096), dtype=float32, sparse=False, ragged=False, name=keras_tensor_19>', '<KerasTensor shape=(None, 4096), dtype=float32, sparse=False, ragged=False, name=keras_tensor_21>')\n  • kwargs=<class 'inspect._empty'>",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNotImplementedError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 14\u001b[39m\n\u001b[32m      7\u001b[39m \u001b[38;5;129m@st\u001b[39m.cache_resource\n\u001b[32m      8\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mload_model\u001b[39m():\n\u001b[32m      9\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m tf.keras.models.load_model(\n\u001b[32m     10\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33msiamesemodel.keras\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     11\u001b[39m         custom_objects={\u001b[33m\"\u001b[39m\u001b[33mL1Dist\u001b[39m\u001b[33m\"\u001b[39m: tf.keras.layers.Layer}\n\u001b[32m     12\u001b[39m     )\n\u001b[32m---> \u001b[39m\u001b[32m14\u001b[39m model = \u001b[43mload_model\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m     16\u001b[39m st.title(\u001b[33m\"\u001b[39m\u001b[33mLive Face Verification\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m     18\u001b[39m run = st.checkbox(\u001b[33m\"\u001b[39m\u001b[33mRun webcam\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\streamlit\\runtime\\caching\\cache_utils.py:219\u001b[39m, in \u001b[36mCachedFunc.__call__\u001b[39m\u001b[34m(self, *args, **kwargs)\u001b[39m\n\u001b[32m    216\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m    217\u001b[39m         spinner_message = \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mRunning `\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mname\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m(...)`.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m--> \u001b[39m\u001b[32m219\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_get_or_create_cached_value\u001b[49m\u001b[43m(\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mspinner_message\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\streamlit\\runtime\\caching\\cache_utils.py:261\u001b[39m, in \u001b[36mCachedFunc._get_or_create_cached_value\u001b[39m\u001b[34m(self, func_args, func_kwargs, spinner_message)\u001b[39m\n\u001b[32m    255\u001b[39m spinner_or_no_context = (\n\u001b[32m    256\u001b[39m     spinner(spinner_message, _cache=\u001b[38;5;28;01mTrue\u001b[39;00m)\n\u001b[32m    257\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m spinner_message \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m is_nested_cache_function\n\u001b[32m    258\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m contextlib.nullcontext()\n\u001b[32m    259\u001b[39m )\n\u001b[32m    260\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m spinner_or_no_context:\n\u001b[32m--> \u001b[39m\u001b[32m261\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_handle_cache_miss\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcache\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mvalue_key\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfunc_args\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfunc_kwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\streamlit\\runtime\\caching\\cache_utils.py:320\u001b[39m, in \u001b[36mCachedFunc._handle_cache_miss\u001b[39m\u001b[34m(self, cache, value_key, func_args, func_kwargs)\u001b[39m\n\u001b[32m    316\u001b[39m \u001b[38;5;66;03m# We acquired the lock before any other thread. Compute the value!\u001b[39;00m\n\u001b[32m    317\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mself\u001b[39m._info.cached_message_replay_ctx.calling_cached_function(\n\u001b[32m    318\u001b[39m     \u001b[38;5;28mself\u001b[39m._info.func\n\u001b[32m    319\u001b[39m ):\n\u001b[32m--> \u001b[39m\u001b[32m320\u001b[39m     computed_value = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_info\u001b[49m\u001b[43m.\u001b[49m\u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43mfunc_args\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mfunc_kwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    322\u001b[39m \u001b[38;5;66;03m# We've computed our value, and now we need to write it back to the cache\u001b[39;00m\n\u001b[32m    323\u001b[39m \u001b[38;5;66;03m# along with any \"replay messages\" that were generated during value computation.\u001b[39;00m\n\u001b[32m    324\u001b[39m messages = \u001b[38;5;28mself\u001b[39m._info.cached_message_replay_ctx._most_recent_messages\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 9\u001b[39m, in \u001b[36mload_model\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m      7\u001b[39m \u001b[38;5;129m@st\u001b[39m.cache_resource\n\u001b[32m      8\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mload_model\u001b[39m():\n\u001b[32m----> \u001b[39m\u001b[32m9\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mtf\u001b[49m\u001b[43m.\u001b[49m\u001b[43mkeras\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmodels\u001b[49m\u001b[43m.\u001b[49m\u001b[43mload_model\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m     10\u001b[39m \u001b[43m        \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43msiamesemodel.keras\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[32m     11\u001b[39m \u001b[43m        \u001b[49m\u001b[43mcustom_objects\u001b[49m\u001b[43m=\u001b[49m\u001b[43m{\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mL1Dist\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m:\u001b[49m\u001b[43m \u001b[49m\u001b[43mtf\u001b[49m\u001b[43m.\u001b[49m\u001b[43mkeras\u001b[49m\u001b[43m.\u001b[49m\u001b[43mlayers\u001b[49m\u001b[43m.\u001b[49m\u001b[43mLayer\u001b[49m\u001b[43m}\u001b[49m\n\u001b[32m     12\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\saving\\saving_api.py:189\u001b[39m, in \u001b[36mload_model\u001b[39m\u001b[34m(filepath, custom_objects, compile, safe_mode)\u001b[39m\n\u001b[32m    186\u001b[39m         is_keras_zip = \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[32m    188\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m is_keras_zip \u001b[38;5;129;01mor\u001b[39;00m is_keras_dir \u001b[38;5;129;01mor\u001b[39;00m is_hf:\n\u001b[32m--> \u001b[39m\u001b[32m189\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43msaving_lib\u001b[49m\u001b[43m.\u001b[49m\u001b[43mload_model\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    190\u001b[39m \u001b[43m        \u001b[49m\u001b[43mfilepath\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    191\u001b[39m \u001b[43m        \u001b[49m\u001b[43mcustom_objects\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcustom_objects\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    192\u001b[39m \u001b[43m        \u001b[49m\u001b[38;5;28;43mcompile\u001b[39;49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mcompile\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[32m    193\u001b[39m \u001b[43m        \u001b[49m\u001b[43msafe_mode\u001b[49m\u001b[43m=\u001b[49m\u001b[43msafe_mode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    194\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    195\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mstr\u001b[39m(filepath).endswith((\u001b[33m\"\u001b[39m\u001b[33m.h5\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33m.hdf5\u001b[39m\u001b[33m\"\u001b[39m)):\n\u001b[32m    196\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m legacy_h5_format.load_model_from_hdf5(\n\u001b[32m    197\u001b[39m         filepath, custom_objects=custom_objects, \u001b[38;5;28mcompile\u001b[39m=\u001b[38;5;28mcompile\u001b[39m\n\u001b[32m    198\u001b[39m     )\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\saving\\saving_lib.py:367\u001b[39m, in \u001b[36mload_model\u001b[39m\u001b[34m(filepath, custom_objects, compile, safe_mode)\u001b[39m\n\u001b[32m    362\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    363\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mInvalid filename: expected a `.keras` extension. \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    364\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mReceived: filepath=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfilepath\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m\"\u001b[39m\n\u001b[32m    365\u001b[39m     )\n\u001b[32m    366\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(filepath, \u001b[33m\"\u001b[39m\u001b[33mrb\u001b[39m\u001b[33m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m--> \u001b[39m\u001b[32m367\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_load_model_from_fileobj\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    368\u001b[39m \u001b[43m        \u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcustom_objects\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mcompile\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msafe_mode\u001b[49m\n\u001b[32m    369\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\saving\\saving_lib.py:444\u001b[39m, in \u001b[36m_load_model_from_fileobj\u001b[39m\u001b[34m(fileobj, custom_objects, compile, safe_mode)\u001b[39m\n\u001b[32m    441\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m zf.open(_CONFIG_FILENAME, \u001b[33m\"\u001b[39m\u001b[33mr\u001b[39m\u001b[33m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m    442\u001b[39m     config_json = f.read()\n\u001b[32m--> \u001b[39m\u001b[32m444\u001b[39m model = \u001b[43m_model_from_config\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    445\u001b[39m \u001b[43m    \u001b[49m\u001b[43mconfig_json\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcustom_objects\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mcompile\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msafe_mode\u001b[49m\n\u001b[32m    446\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    448\u001b[39m all_filenames = zf.namelist()\n\u001b[32m    449\u001b[39m extract_dir = \u001b[38;5;28;01mNone\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\saving\\saving_lib.py:433\u001b[39m, in \u001b[36m_model_from_config\u001b[39m\u001b[34m(config_json, custom_objects, compile, safe_mode)\u001b[39m\n\u001b[32m    431\u001b[39m \u001b[38;5;66;03m# Construct the model from the configuration file in the archive.\u001b[39;00m\n\u001b[32m    432\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m ObjectSharingScope():\n\u001b[32m--> \u001b[39m\u001b[32m433\u001b[39m     model = \u001b[43mdeserialize_keras_object\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    434\u001b[39m \u001b[43m        \u001b[49m\u001b[43mconfig_dict\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcustom_objects\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msafe_mode\u001b[49m\u001b[43m=\u001b[49m\u001b[43msafe_mode\u001b[49m\n\u001b[32m    435\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    436\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m model\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\saving\\serialization_lib.py:718\u001b[39m, in \u001b[36mdeserialize_keras_object\u001b[39m\u001b[34m(config, custom_objects, safe_mode, **kwargs)\u001b[39m\n\u001b[32m    716\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m custom_obj_scope, safe_mode_scope:\n\u001b[32m    717\u001b[39m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m--> \u001b[39m\u001b[32m718\u001b[39m         instance = \u001b[38;5;28;43mcls\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mfrom_config\u001b[49m\u001b[43m(\u001b[49m\u001b[43minner_config\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    719\u001b[39m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[32m    720\u001b[39m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\n\u001b[32m    721\u001b[39m             \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mcls\u001b[39m\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m could not be deserialized properly. Please\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    722\u001b[39m             \u001b[33m\"\u001b[39m\u001b[33m ensure that components that are Python object\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m   (...)\u001b[39m\u001b[32m    726\u001b[39m             \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[33mconfig=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mconfig\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m.\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[33mException encountered: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00me\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m\"\u001b[39m\n\u001b[32m    727\u001b[39m         )\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\models\\model.py:587\u001b[39m, in \u001b[36mModel.from_config\u001b[39m\u001b[34m(cls, config, custom_objects)\u001b[39m\n\u001b[32m    582\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m is_functional_config \u001b[38;5;129;01mand\u001b[39;00m revivable_as_functional:\n\u001b[32m    583\u001b[39m     \u001b[38;5;66;03m# Revive Functional model\u001b[39;00m\n\u001b[32m    584\u001b[39m     \u001b[38;5;66;03m# (but not Functional subclasses with a custom __init__)\u001b[39;00m\n\u001b[32m    585\u001b[39m     \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mkeras\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01msrc\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmodels\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mfunctional\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m functional_from_config\n\u001b[32m--> \u001b[39m\u001b[32m587\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunctional_from_config\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    588\u001b[39m \u001b[43m        \u001b[49m\u001b[38;5;28;43mcls\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mconfig\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcustom_objects\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcustom_objects\u001b[49m\n\u001b[32m    589\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    591\u001b[39m \u001b[38;5;66;03m# Either the model has a custom __init__, or the config\u001b[39;00m\n\u001b[32m    592\u001b[39m \u001b[38;5;66;03m# does not contain all the information necessary to\u001b[39;00m\n\u001b[32m    593\u001b[39m \u001b[38;5;66;03m# revive a Functional model. This happens when the user creates\u001b[39;00m\n\u001b[32m   (...)\u001b[39m\u001b[32m    596\u001b[39m \u001b[38;5;66;03m# In this case, we fall back to provide all config into the\u001b[39;00m\n\u001b[32m    597\u001b[39m \u001b[38;5;66;03m# constructor of the class.\u001b[39;00m\n\u001b[32m    598\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\models\\functional.py:576\u001b[39m, in \u001b[36mfunctional_from_config\u001b[39m\u001b[34m(cls, config, custom_objects)\u001b[39m\n\u001b[32m    574\u001b[39m node_data = node_data_list[node_index]\n\u001b[32m    575\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m--> \u001b[39m\u001b[32m576\u001b[39m     \u001b[43mprocess_node\u001b[49m\u001b[43m(\u001b[49m\u001b[43mlayer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnode_data\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    578\u001b[39m \u001b[38;5;66;03m# If the node does not have all inbound layers\u001b[39;00m\n\u001b[32m    579\u001b[39m \u001b[38;5;66;03m# available, stop processing and continue later\u001b[39;00m\n\u001b[32m    580\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mIndexError\u001b[39;00m:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\models\\functional.py:506\u001b[39m, in \u001b[36mfunctional_from_config.<locals>.process_node\u001b[39m\u001b[34m(layer, node_data)\u001b[39m\n\u001b[32m    503\u001b[39m args, kwargs = deserialize_node(node_data, created_layers)\n\u001b[32m    504\u001b[39m \u001b[38;5;66;03m# Call layer on its inputs, thus creating the node\u001b[39;00m\n\u001b[32m    505\u001b[39m \u001b[38;5;66;03m# and building the layer if needed.\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m506\u001b[39m \u001b[43mlayer\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\utils\\traceback_utils.py:122\u001b[39m, in \u001b[36mfilter_traceback.<locals>.error_handler\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    119\u001b[39m     filtered_tb = _process_traceback_frames(e.__traceback__)\n\u001b[32m    120\u001b[39m     \u001b[38;5;66;03m# To get the full stack trace, call:\u001b[39;00m\n\u001b[32m    121\u001b[39m     \u001b[38;5;66;03m# `keras.config.disable_traceback_filtering()`\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m122\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m e.with_traceback(filtered_tb) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m    123\u001b[39m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[32m    124\u001b[39m     \u001b[38;5;28;01mdel\u001b[39;00m filtered_tb\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\myenv\\Lib\\site-packages\\keras\\src\\layers\\layer.py:953\u001b[39m, in \u001b[36mLayer.call\u001b[39m\u001b[34m(self, *args, **kwargs)\u001b[39m\n\u001b[32m    952\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mcall\u001b[39m(\u001b[38;5;28mself\u001b[39m, *args, **kwargs):\n\u001b[32m--> \u001b[39m\u001b[32m953\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m._not_implemented_error(\u001b[38;5;28mself\u001b[39m.call)\n",
      "\u001b[31mNotImplementedError\u001b[39m: Exception encountered when calling Layer.call().\n\n\u001b[1mCould not automatically infer the output shape / dtype of 'l1_dist_17' (of type Layer). Either the `Layer.call()` method is incorrect, or you need to implement the `Layer.compute_output_spec() / compute_output_shape()` method. Error encountered:\n\nLayer Layer does not have a `call` method implemented.\u001b[0m\n\nArguments received by Layer.call():\n  • args=('<KerasTensor shape=(None, 4096), dtype=float32, sparse=False, ragged=False, name=keras_tensor_19>', '<KerasTensor shape=(None, 4096), dtype=float32, sparse=False, ragged=False, name=keras_tensor_21>')\n  • kwargs=<class 'inspect._empty'>"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import cv2\n",
    "import numpy as np\n",
    "import tensorflow as tf\n",
    "\n",
    "# Load your saved Siamese model\n",
    "@st.cache_resource\n",
    "def load_model():\n",
    "    return tf.keras.models.load_model(\n",
    "        \"siamesemodel.keras\",\n",
    "        custom_objects={\"L1Dist\": tf.keras.layers.Layer}\n",
    "    )\n",
    "\n",
    "model = load_model()\n",
    "\n",
    "st.title(\"Live Face Verification\")\n",
    "\n",
    "run = st.checkbox(\"Run webcam\")\n",
    "FRAME_WINDOW = st.image([])\n",
    "\n",
    "if run:\n",
    "    cap = cv2.VideoCapture(0)  # usually 0 for your default camera\n",
    "    while run:\n",
    "        ret, frame = cap.read()\n",
    "        if not ret:\n",
    "            st.error(\"Unable to read from webcam\")\n",
    "            break\n",
    "\n",
    "        # Show frame in Streamlit\n",
    "        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))\n",
    "\n",
    "        if st.button(\"Verify\"):\n",
    "            # Preprocess your frame here, e.g. resize to 100×100 and normalize\n",
    "            img = cv2.resize(frame, (100,100))\n",
    "            img = img.astype(np.float32) / 255.0\n",
    "            img = np.expand_dims(img, axis=0)\n",
    "\n",
    "            # For demo: compare against a stored \"anchor\" sample\n",
    "            # (you’d load and preprocess your anchor similarly)\n",
    "            anchor = img  # replace with real anchor\n",
    "            \n",
    "            # Predict distance\n",
    "            dist = model.predict([anchor, img])[0][0]\n",
    "            st.write(f\"Distance: {dist:.3f}\")\n",
    "            st.write(\"Verified!\" if dist < 0.5 else \"Not verified\")\n",
    "    cap.release()\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (myenv)",
   "language": "python",
   "name": "myenv"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
