---
title: API Reference
description: Complete API reference for the lexigram-ai-evaluation package.
sidebar:
  hidden: true
head:
  - tag: style
    content: |
      .sl-markdown-content p,
      .sl-markdown-content li,
      .sl-markdown-content td,
      .sl-markdown-content th,
      .sl-markdown-content blockquote,
      .sl-markdown-content dt,
      .sl-markdown-content dd {
        font-family: var(--sl-font-mono) !important;
        font-size: 0.9rem;
        line-height: 1.65;
      }
      .sl-markdown-content code {
        font-size: 0.88em;
      }
---

## Classes


<div data-pagefind-weight='10'>

### `BatchEvaluationResult`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/types.py#L38' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Result of running evaluation on multiple samples.

Contains aggregated results and per-sample details.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluationConfig`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/config.py#L15' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Configuration for the evaluation subsystem.

Attributes:
    enabled: Enable the AI evaluation subsystem.
    default_threshold: Default score threshold for passing evaluations.
    embedding_model: Model to use for embedding-based evaluations.
    include_metadata: Whether to include metadata in run reports.
    max_samples: Maximum number of samples per evaluation run.
    max_retries: Maximum retries for failed evaluations.
    timeout_seconds: Timeout for evaluation execution in seconds.

Example

```python
config = EvaluationConfig(
    default_threshold=0.9,
    embedding_model="text-embedding-3-large"
)
```


    config = EvaluationConfig(
        default_threshold=0.9,
        embedding_model="text-embedding-3-large"
    )

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluationDataset`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/ai/evaluation.py#L59' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
A collection of evaluation samples.

Attributes:
    name: Name of the dataset.
    samples: List of evaluation samples.
    metadata: Additional dataset metadata.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluationModule`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/module.py#L18' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Evaluation module for Lexigram applications.

Provides evaluator and harness support for AI model evaluation.

Usage

```python
from lexigram.ai.evaluation import EvaluationModule
from lexigram.ai.evaluation.config import EvaluationConfig

@module(
    imports=[EvaluationModule.configure(EvaluationConfig(...))]
)
class AppModule(Module):
    pass
```


    from lexigram.ai.evaluation import EvaluationModule
    from lexigram.ai.evaluation.config import EvaluationConfig

    @module(
        imports=[EvaluationModule.configure(EvaluationConfig(...))]
    )
    class AppModule(Module):
        pass

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>configure</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>configure</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>cls</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>config</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-evaluation/api/#evaluationconfig' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>EvaluationConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>DynamicModule</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/module.py#L36' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Create an EvaluationModule with explicit configuration.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`config`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-evaluation/api/#evaluationconfig' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>EvaluationConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-evaluation/api/#evaluationconfig' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>EvaluationConfig</a> or ``None`` for defaults.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>DynamicModule</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A DynamicModule descriptor.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>stub</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>stub</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>cls</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>config</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-evaluation/api/#evaluationconfig' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>EvaluationConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>DynamicModule</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/module.py#L58' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Create an EvaluationModule suitable for unit and integration testing.

Uses in-memory or no-op evaluator implementations with minimal side
effects.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`config`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-evaluation/api/#evaluationconfig' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>EvaluationConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional <a href='/platform/lexigram-ai-evaluation/api/#evaluationconfig' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>EvaluationConfig</a> override. Uses safe test defaults when ``None``.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>DynamicModule</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A DynamicModule descriptor.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluationProvider`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/di/provider.py#L22' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Registers evaluation services with the DI container.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>config</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-evaluation/api/#evaluationconfig' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>EvaluationConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/di/provider.py#L30' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>register</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>register</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>container</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>ContainerRegistrarProtocol</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/di/provider.py#L35' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>boot</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>boot</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>container</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>BootContainerProtocol</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/di/provider.py#L73' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>shutdown</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>shutdown</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/di/provider.py#L76' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>health_check</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>health_check</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>timeout</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>5.0</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>HealthCheckResult</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/di/provider.py#L79' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluationResult`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/ai/evaluation.py#L25' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Result of an evaluation run on a single sample.

Attributes:
    score: The evaluation score (0.0 to 1.0).
    score_type: The type of scoring method used.
    feedback: Human-readable feedback about the evaluation.
    metrics: Additional metrics computed during evaluation.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluationRunContext`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/types.py#L21' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Context for a single evaluation run.

Holds the dataset, evaluator, and configuration for an evaluation run.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluationSample`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/ai/evaluation.py#L42' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
A single sample in an evaluation dataset.

Attributes:
    id: Unique identifier for this sample.
    input: The input prompt or query.
    reference: The expected reference output.
    metadata: Additional metadata for this sample.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `RunReport`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/ai/evaluation.py#L74' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Report from running an evaluator on a dataset.

Attributes:
    dataset_name: Name of the evaluated dataset.
    evaluator_name: Name of the evaluator used.
    total_samples: Total number of samples evaluated.
    passed_samples: Number of samples that passed the evaluation.
    average_score: Average score across all samples.
    results: Individual sample results.
    metadata: Additional report metadata.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

## Exceptions


<div data-pagefind-weight='10'>

### `DatasetError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/exceptions.py#L16' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Raised when there's an error with the evaluation dataset.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluationConfigError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/exceptions.py#L8' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Raised when evaluation configuration is invalid.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `EvaluatorNotFoundError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/exceptions.py#L12' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Raised when a requested evaluator cannot be found.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `HarnessError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-ai-evaluation/src/lexigram/ai/evaluation/exceptions.py#L20' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Raised when the evaluation harness encounters an error.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />
