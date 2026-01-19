# AI Agent

A shell tool to enable agentic flows with remote LLM APIs while executing tools and executing generating code locally. Similar to Claude Code, OpenAI Codex, and OpenCode.

## Built with

- [Python](https://www.python.org/)
- [UV](https://docs.astral.sh/uv/)
- [Google Gen AI](https://pypi.org/project/google-genai/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

## TODO

- [ ] Config Python Formatter
- [ ] Config Python Type Checker
- [ ] Config Logging

## Links

- https://models.dev/
- https://aistudio.google.com

## Example Google genai client model generate_content result

[GenerateContentResponse](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse)

```py
candidates=[Candidate(content=Content(parts=[Part(video_metadata=None, thought=None, code_execution_result=None, executable_code=None, file_data=None, function_call=None, function_response=None, inline_data=None, text='4')], role='model'), citation_metadata=None, finish_message=None, token_count=None, finish_reason=<FinishReason.STOP: 'STOP'>, avg_logprobs=None, grounding_metadata=None, index=0, logprobs_result=None, safety_ratings=None)] create_time=None response_id=None model_version='gemini-2.5-flash' prompt_feedback=None usage_metadata=GenerateContentResponseUsageMetadata(cache_tokens_details=None, cached_content_token_count=None, candidates_token_count=1, candidates_tokens_details=None, prompt_token_count=10, prompt_tokens_details=[ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=10)], thoughts_token_count=34, tool_use_prompt_token_count=None, tool_use_prompt_tokens_details=None, total_token_count=45, traffic_type=None) automatic_function_calling_history=[] parsed=None
```
