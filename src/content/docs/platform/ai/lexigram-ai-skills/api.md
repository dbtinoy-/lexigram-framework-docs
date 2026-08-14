---
title: API Reference
description: Explore the complete API reference for the lexigram-ai-skills package. Discover protocols, classes, and methods for building with Lexigram.
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

## Protocols


<div data-pagefind-weight='10'>

### `SkillExecutorProtocol`

</div>

<span data-api-type='Protocols' style='display:none;'></span>


Protocol for executing skills with lifecycle management.

Handles skill selection, validation, execution, retry, caching,
permission checking, and observability.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>user_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>session_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute a skill with full lifecycle management.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill to execute</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameters for the skill</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`user_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional user ID for permission checks</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`session_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional session ID for context</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Result with SkillResult on success or SkillError on failure</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillProtocol`

</div>

<span data-api-type='Protocols' style='display:none;'></span>


Protocol for a composable skill.

A skill is an async-callable capability that can be registered,
discovered, and executed with validation and error handling.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Get the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The skill's definition including parameters and metadata</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute the skill.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Result with SkillResult on success or SkillError on failure</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>validate</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Validate parameters against the definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameters to validate</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of validation errors (empty if valid)</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillRegistryProtocol`

</div>

<span data-api-type='Protocols' style='display:none;'></span>


Protocol for registering and discovering skills.

Maintains a registry of available skills with support for
filtering by category and permissions.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>register</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>skill</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillProtocol</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Register a skill in the registry.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillProtocol</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The skill to register</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>get</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skillprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillProtocol</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span></pre></div>

Get a skill by name.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The skill name</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillProtocol</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The skill, or None if not found</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>list_skills</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>category</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>permissions</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

List available skills with optional filtering.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`category`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Filter by skill category</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`permissions`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Filter to skills that match any of these permissions</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of skill definitions matching the criteria</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>get_schemas</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Get OpenAI function-calling compatible schemas.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of skill schemas in OpenAI function calling format</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

## Classes


<div data-pagefind-weight='10'>

### `AbstractSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Abstract base class for class-based skill definitions.

Subclass this and define a ``definition`` class attribute plus an
``execute`` method.  Parameter validation default uses the JSON schema
stored on the definition; override ``validate`` for custom rules.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute the skill with the provided keyword arguments.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Result wrapping SkillResult on success or SkillError on failure.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>validate</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Validate *params* against the skill definition's parameter schema.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameters to validate.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of validation error messages (empty list means valid).</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>to_tool</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>SkillToolAdapter</span></pre></div>

Convert this skill to a ToolProtocol for use in Lexigram agents.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>SkillToolAdapter</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A SkillToolAdapter that implements ToolProtocol.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `CodeExecutionSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Execute code in a sandboxed environment and return the output.

This is a stub implementation.  For production use, replace with a
proper sandboxed execution backend (e.g. Docker, WASM, a remote
code execution service).

Required permission: ``code.execute``.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the code_execute skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Return a stub result indicating execution is not implemented.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok stub result with ``output=""``, ``stderr=""``, ``exit_code=0``, and ``stub=True``.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `DatabaseQuerySkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Execute read-only SELECT statements and return row dicts.

Only ``SELECT`` statements are accepted.  A ``LIMIT`` clause is
automatically appended when the query does not already contain one,
capped at *max_rows* (default 100) to prevent runaway reads.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`db`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A DatabaseProviderProtocol instance.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`max_rows`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Maximum rows returned per query.</td></tr></tbody></table></div>



<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>db</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>DatabaseProviderProtocol</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>max_rows</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>int</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>_DEFAULT_LIMIT</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise the skill with a database provider.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`db`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>DatabaseProviderProtocol</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>DatabaseProviderProtocol for query execution.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`max_rows`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Hard cap on returned rows.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the database_query skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute the SELECT query and return up to *max_rows* rows.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok result with ``rows`` and ``row_count``, or Err if the query is not a SELECT or execution fails.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `DateTimeSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Return the current UTC date, time, and Unix timestamp.

Parameters
----------
timezone : str, optional
    IANA timezone name (e.g. ``"America/New_York"``).  Defaults to
    ``"UTC"``.  Only UTC is supported without the ``zoneinfo`` stdlib
    module (Python 3.9+); unknown timezones fall back to UTC.

Example output

```python
{
  "datetime": "2026-01-15T14:32:00+00:00",
  "date": "2026-01-15",
  "time": "14:32:00",
  "timestamp": 1736951520.0,
  "timezone": "UTC"
}
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the current_datetime skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute the skill and return the current datetime.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok result containing a datetime dict.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `FileReadSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Read a file and return its content as a string.

Files are only accessible within *base_dir* (defaults to the current
working directory).  Directory traversal attempts return an error.

Required permission: ``files.read``.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>base_dir</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with an optional sandbox directory.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`base_dir`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Base directory constraint.  Defaults to ``os.getcwd()``.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the file_read skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Read and return file content.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok result with ``content``, ``path``, and ``size_bytes``, or Err.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `FileWriteSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Write text content to a local file.

Files are only writable within *base_dir*.  The parent directory must
exist; write will not create intermediate directories.

Required permission: ``files.write``.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>base_dir</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with an optional sandbox directory.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`base_dir`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Base directory constraint.  Defaults to ``os.getcwd()``.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the file_write skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Write content to the specified path.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok result with ``path`` and ``bytes_written``, or Err.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `FunctionSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Wraps an async function decorated with ``@skill`` as a SkillProtocol.

Created automatically by the ``@skill`` decorator — not intended for
direct instantiation.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>fn</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Callable<span style='color: var(--lex-color-colon)'>[</span>Ellipsis<span style='color: var(--lex-color-colon)'>,</span> Awaitable<span style='color: var(--lex-color-colon)'>[</span>Any<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>definition</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>param_names</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise a FunctionSkill.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`fn`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Callable<span style='color: var(--lex-color-colon)'>[</span>Ellipsis<span style='color: var(--lex-color-colon)'>,</span> Awaitable<span style='color: var(--lex-color-colon)'>[</span>Any<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The underlying async callable.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`definition`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The skill's definition metadata.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`param_names`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ordered list of declared parameter names from ``@skill_param`` decorators (used for schema building).</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The SkillDefinition for this function skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Call the wrapped async function and wrap its return value.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Result wrapping SkillResult on success or SkillError on failure.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>validate</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Validate *params* against the JSON schema in the definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameters to validate.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of validation error messages.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>to_tool</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>SkillToolAdapter</span></pre></div>

Convert this skill to a ToolProtocol for use in Lexigram agents.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>SkillToolAdapter</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A SkillToolAdapter that implements ToolProtocol.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `HTTPRequestSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Make outbound HTTP requests and return the response body.

By default the skill uses urllib.request (stdlib) to avoid
requiring an extra HTTP client dependency.  For production workloads
integrate with the ``lexigram-http`` ``HTTPClientProtocol``.

Required permission: ``http.request``.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the http_request skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute the HTTP request (stdlib urllib, sync-in-thread).



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok result with ``status_code``, ``body``, and ``url``, or Err on network/validation failure.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MCPSkillBridge`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Import MCP tools as Lexigram skills and export skills as MCP tools.

This bridge allows a skill registry to expose its skills to MCP-aware
callers and consume MCP tools as if they were first-class skills.


**Note**

The MCP integration uses lexigram.ai.mcp when available.
This class is a stub that gracefully degrades when the MCP package
is not installed.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>registry</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise the bridge with the backing registry.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`registry`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The skill registry to import into / export from.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>import_from_mcp</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>mcp_client</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>int</span></pre></div>

Register all tools exposed by an MCP client as skills.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`mcp_client`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>An object implementing MCPClientProtocol (from ``lexigram.ai.mcp``).</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Number of tools successfully imported as skills.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>get_mcp_tool_definitions</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Export all registered skills as MCP tool definitions.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of dicts following the MCP tool definition schema.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MathSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Evaluate safe arithmetic expressions.

Supports the operators ``+``, ``-``, ``*``, ``/``, ``//``, ``%``, and
``**``.  No functions, names, or string literals are permitted.

Example output

```python
{"result": 1024.0, "expression": "2 ** 10"}
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the math_calculate skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Evaluate the expression and return the result.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok result with ``result`` and ``expression`` keys, or Err on invalid expression.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `ModuleScanner`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Discover and auto-register skills from Python modules.

The scanner walks every attribute of the target module.  Attributes that
are instances of BaseSkill (or its subclasses, including
<a href='/platform/lexigram-ai-skills/api/#functionskill' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>FunctionSkill</a>) are registered into the provided
<a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a>.

Example

```python
scanner = ModuleScanner(container)
await scanner.scan(registry, "myapp.skills.builtin")
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>container</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/foundation/lexigram-contracts/api/#containerprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ContainerProtocol</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise the scanner.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`container`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/foundation/lexigram-contracts/api/#containerprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ContainerProtocol</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional DI container for resolving class-based skills.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>scan</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>registry</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>module_path</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>int</span></pre></div>

Import *module_path* and register all discovered skills.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`registry`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The <a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a> to register discovered skills into.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`module_path`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Dotted import path of the module to scan.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Number of skills successfully registered.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>scan_package</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>registry</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>package_path</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>int</span></pre></div>

Recursively scan all modules within a package.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`registry`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The <a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a> to register discovered skills into.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`package_path`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Dotted import path of the package to scan.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Total number of skills registered across all sub-modules.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `ParallelSkills`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Execute multiple skills concurrently and aggregate their outputs.

All skills receive the same *params*.  Errors from individual skills do
not abort the fan-out; they are collected and returned as part of the
aggregated output dict under an ``"_errors"`` key.

Example

```python
parallel = ParallelSkills(["sentiment_analysis", "entity_extraction"])
result = await parallel.execute(executor, {"text": "Hello world"})
combined = result.unwrap().output
# combined == {"sentiment_analysis": {...}, "entity_extraction": {...}}
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>skill_names</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with the skills to run in parallel.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_names`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Names of skills to execute concurrently.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>executor</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Run all skills concurrently and aggregate results.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`executor`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillExecutorProtocol instance.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Input parameters forwarded to every skill.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A SkillResult whose ``output`` is a dict mapping each skill name to its output (or an error string if that skill failed).</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `PermissionChecker`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Grant and verify per-user permission sets for skill execution.

Permissions are plain strings (e.g. ``"files.read"``, ``"db.query"``).
A user with no registered permissions is treated as having *no* permissions.

Example

```python
checker = PermissionChecker()
checker.grant("user-123", {"files.read", "web.search"})
allowed = checker.check("user-123", {"files.read"})   # True
denied  = checker.check("user-123", {"db.write"})     # False
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise an empty permission store.

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>grant</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>user_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>permissions</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Add permissions for a user.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`user_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The user identifier.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`permissions`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Set of permission strings to grant.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>revoke</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>user_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>permissions</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Remove permissions for a user.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`user_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The user identifier.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`permissions`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Set of permission strings to revoke.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>set_permissions</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>user_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>permissions</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Replace all permissions for a user with the given set.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`user_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The user identifier.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`permissions`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Complete replacement permission set.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>get_permissions</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>user_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Return the current permission set for a user.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`user_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The user identifier.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Set of permission strings (may be empty).</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>check</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>user_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>required</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>bool</span></pre></div>

Check whether a user possesses *all* required permissions.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`user_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The user to check.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`required`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>set<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Permissions that must all be present.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>bool</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>``True`` if every required permission is granted; ``False`` otherwise (including when *required* is empty — returns ``True``).</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillChain`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Execute skills sequentially, piping each output into the next input.

Each step is a ``(skill_name, output_mapping)`` tuple where
*output_mapping* maps keys from the previous output dict to parameter
names for the next skill.  An empty mapping passes all keys unchanged.

Example

```python
chain = SkillChain([
    ("web_search", {"results": "documents"}),
    ("text_summarize", {}),
])
result = await chain.execute(executor, {"query": "AI trends 2026"})
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>steps</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>tuple<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> str<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise the chain with its steps.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`steps`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>tuple<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> str<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of ``(skill_name, output_to_input_mapping)`` tuples.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>executor</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>initial_params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute the chain from *initial_params*.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`executor`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillExecutorProtocol instance used to run each step.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`initial_params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameters passed to the first skill.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Result from the final step, or the first error encountered.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillDefinition`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Definition of a skill's interface and behavior.

Attributes:
    name: Unique skill name
    description: What the skill does
    parameters_schema: JSON Schema for parameters
    returns_schema: JSON Schema for return value
    category: Skill category for organization
    requires_confirmation: If True, requires user approval before execution
    cacheable: Whether results can be cached
    max_retries: Maximum retry attempts on failure
    timeout_seconds: Execution timeout in seconds
    permissions: Required permissions to execute

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillExecutedEvent`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Emitted when a skill execution completes (success or failure).

Consumed by: audit, analytics, skill performance monitoring.

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillExecutedHook`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Payload fired when a skill executor completes a skill call.

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillExecutionFailedHook`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Payload fired when a skill executor records a failed skill call.

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillExecutor`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Executes skills with the full production lifecycle.

Handles skill resolution, permission checking, parameter validation,
result caching, retry with exponential backoff, timeout enforcement,
and observability logging.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>registry</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillregistryprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistryProtocol</a></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>*</span><span style='color: var(--lex-color-name)'></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>cache</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>CacheBackendProtocol <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>permission_checker</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>PermissionCheckerProtocol <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>semaphore</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>asyncio.Semaphore <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise the executor.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`registry`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillregistryprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistryProtocol</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillRegistryProtocol implementation.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`cache`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>CacheBackendProtocol <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional CacheBackendProtocol for caching deterministic results.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`permission_checker`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>PermissionCheckerProtocol <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional PermissionCheckerProtocol for access control.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`semaphore`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>asyncio.Semaphore <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional semaphore limiting concurrent executions.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>user_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>session_id</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute a skill with full lifecycle management.

Steps: resolve → check permissions → validate → check cache →
execute with retry → store cache → return.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Registered name of the skill to execute.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Skill parameters.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`user_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional caller identity for permission checks.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`session_id`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional session context (passed through to metadata).</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Result wrapping SkillResult on success or SkillError on failure.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillLoader`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Handles loading bundled files and executing skill scripts.

Features:
- Reading reference.md, forms.md, and other bundled context files
- Executing scripts (Python, Shell, JavaScript) with parameters
- Sandboxed execution with path validation
- Timeout enforcement
- Environment variable injection

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>sandbox</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>bool</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>True</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>timeout_seconds</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>int</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>30</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>max_file_size</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>int</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>1024 * 1024</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialize the loader.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`sandbox`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>bool</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Whether to enable sandboxing (default: True).</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`timeout_seconds`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Script execution timeout (default: 30s).</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`max_file_size`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Maximum file size for context loading (default: 1MB).</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>load_bundled_file</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>path</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Path</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span></pre></div>

Load a bundled context file with size limit.

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>load_bundled_context</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_dir</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Path</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>context_files</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Load multiple bundled context files.

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute_script</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>script_path</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Path</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Execute a skill script with parameters.
</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillPipeline`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Apply a sequence of skills as transformation stages to the same payload.

Unlike <a href='/platform/lexigram-ai-skills/api/#skillchain' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillChain</a> which passes the *output* of one skill as the
*input* of the next, a pipeline enriches a single mutable context dict;
each stage may read from and write to that shared context.

Example

```python
pipeline = SkillPipeline()
pipeline.add_stage("normalise_text", output_key="clean")
pipeline.add_stage("extract_entities", output_key="entities")
result = await pipeline.execute(executor, {"raw_text": "..."})
# result.unwrap().output == {"raw_text": ..., "clean": ..., "entities": ...}
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise an empty pipeline.

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>add_stage</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>output_key</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Append a stage to the pipeline.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Skill to invoke at this stage.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`output_key`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>If given, the skill's output is stored in the shared context under this key.  If ``None`` the output dict is merged into the context (ignored for non-dict outputs).</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>executor</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>initial_context</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Run the pipeline.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`executor`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillExecutorProtocol instance.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`initial_context`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Shared context passed to (and enriched by) each stage.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A SkillResult whose ``output`` is the final enriched context, or the first error encountered.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillRegisteredHook`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Payload fired when a skill registry adds a skill definition.

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillRegistry`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Central registry for all available skills.

Supports registration, lookup by name, category-based listing,
permission-filtered listing, and OpenAI function-calling schema export.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise an empty registry.

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>register</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>skill</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillProtocol</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Register a skill.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillProtocol</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The skill to register.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Raises</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Exception</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillalreadyregisterederror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillAlreadyRegisteredError</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>If a skill with the same name is already registered.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>register_tool</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>tool</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/foundation/lexigram-contracts/api/#toolprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ToolProtocol</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Wrap *tool* as a <a href='/platform/lexigram-ai-skills/api/#toolskilladapter' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ToolSkillAdapter</a> and register it.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`tool`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/foundation/lexigram-contracts/api/#toolprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ToolProtocol</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Any object satisfying ToolProtocol.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>get</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skillprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillProtocol</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span></pre></div>

Return the skill registered under *name*, or ``None``.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Skill name to look up.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillProtocol</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The skill or None if not found.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>list_skills</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>category</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>permissions</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

List registered skill definitions with optional filters.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`category`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Return only skills in this category.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`permissions`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Return only skills whose required permissions are a subset of the supplied permission set.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Matching skill definitions.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>get_schemas</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Return OpenAI function-calling compatible schemas for all skills.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of schema dicts in OpenAI ``tools`` format.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillResult`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Result of a skill execution.

Attributes:
    skill_name: Name of the executed skill
    success: Whether execution succeeded
    output: The output value (if successful)
    error: Error message (if failed)
    duration_ms: Time taken to execute
    cached: Whether result came from cache
    metadata: Additional execution metadata

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillResultCache`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Two-tier result cache for skill executions.

The first tier is an in-process ``dict``; the second tier is an optional
CacheBackendProtocol (e.g. Redis).  Lookups check the in-process dict
first; on a miss they query the backend and populate the in-process dict.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`backend`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional async cache backend for cross-process caching.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`ttl_seconds`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Time-to-live for backend entries in seconds.</td></tr></tbody></table></div>



<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>backend</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>CacheBackendProtocol <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>ttl_seconds</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>int</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>3600</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise the cache.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`backend`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>CacheBackendProtocol <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional CacheBackendProtocol for distributed caching.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`ttl_seconds`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>TTL for backend cache entries.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>get</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span></pre></div>

Return a cached result for the given skill invocation.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameters the skill was called with.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The cached <a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a> or ``None`` when not cached.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>set</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>result</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Store a skill result in both cache tiers.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameters the skill was called with.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`result`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The <a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a> to cache.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>invalidate</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Remove a single entry from the local in-process cache.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameters identifying the entry to remove.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>clear</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Remove all entries from the local in-process cache.
</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillRouter`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Route an input to one of several skills depending on runtime conditions.

Routes are evaluated in registration order; the first match wins.
An optional *fallback* skill name is used when no route matches.

Example

```python
router = SkillRouter(fallback="default_handler")
router.add_route(
    skill_name="premium_search",
    condition=lambda p: p.get("tier") == "premium",
)
router.add_route(
    skill_name="basic_search",
    condition=lambda p: True,        # catch-all
)
result = await router.execute(executor, {"query": "...", "tier": "free"})
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>fallback</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise the router.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`fallback`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Skill name to use when no route matches.  If ``None`` and no route matches, the execution returns an error.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>add_route</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>condition</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Condition</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Register a route.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill to invoke if *condition* returns True.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`condition`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Condition</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Callable receiving the input ``dict`` returning ``bool``.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>executor</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Dispatch *params* to the first matching skill.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`executor`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillExecutorProtocol instance.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Input parameters used both for condition evaluation and forwarded to the resolved skill.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Result from the matched skill, or a SkillRoutingError when no route matches and no fallback is configured.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillSourceScanner`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Discovers and registers SKILL.md-based skills.

Features:
- YAML frontmatter parsing (name, description, version, author, tags)
- $ARGUMENTS placeholder substitution
- Instruction-only skills (skill body as instructions)
- Executable skills (scripts/main.py)
- Bundled context files (reference.md, forms.md, etc.)
- Configurable max depth for nested discovery

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>loader</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillloader' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillLoader</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>max_depth</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>int <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>5</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialize the scanner.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`loader`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillloader' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillLoader</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional SkillLoader for executing scripts.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`max_depth`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Maximum directory depth to scan (None for unlimited).</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>scan</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>registry</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>root</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> Path</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>int</span></pre></div>

Scan a directory tree for SKILL.md folders and register them.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`registry`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillregistry' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillRegistry</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The SkillRegistry to register discovered skills.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`root`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> Path</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Root directory to scan.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Number of skills successfully registered.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillsConfig`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Configuration for the skills subsystem.

Controls execution defaults, caching behaviour, permission enforcement,
auto-discovery settings, and which built-in skills are enabled.

Attributes:
    name: Logical name used for DI registration keys.
    default_timeout_seconds: Default execution timeout per skill.
    max_retries: Default maximum retry attempts for skill execution.
    max_concurrent_executions: Semaphore cap on concurrent executions.
    cache_enabled: Whether result caching is globally enabled.
    cache_ttl_seconds: Default TTL for cached skill results.
    cache_backend: Which cache backend to use (``in_memory``, ``cache``).
    enforce_permissions: Whether permission checks are enforced.
    auto_discover: Whether to auto-scan packages on boot.
    scan_packages: Fully-qualified package names to scan for skills.
    enable_builtin: Whether built-in skills are registered on boot.
    builtin_skills: Names of built-in skills to register.

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillsModule`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Application-level façade for the skills subsystem.

Provides a ``configure`` factory that creates a pre-configured
<a href='/platform/lexigram-ai-skills/api/#skillsprovider' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsProvider</a> ready for registration with the application
container.

Usage

```python
from lexigram.ai.skills import SkillsModule
from lexigram.ai.skills.config import SkillsConfig

@module(
    imports=[SkillsModule.configure(
        SkillsConfig(
            enable_builtin=True,
            builtin_skills=["current_datetime", "math_calculate"],
        )
    )]
)
class AppModule(Module):
    pass
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>configure</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>cls</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>config</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillsconfig' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>enable_tool_bridge</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>bool</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>False</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/packages/foundation/lexigram/api/#dynamicmodule' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>DynamicModule</a></span></pre></div>

Create a SkillsModule with explicit configuration.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`config`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillsconfig' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillsconfig' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsConfig</a> or ``None`` to use defaults.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`enable_tool_bridge`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>bool</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Register the tool-bridge adapter so agent tool registries can invoke skills as first-class tools. Defaults to ``False``. **kwargs: Additional keyword arguments forwarded to <a href='/platform/lexigram-ai-skills/api/#skillsprovider' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsProvider</a>.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/foundation/lexigram/api/#dynamicmodule' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>DynamicModule</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A <a href='/packages/foundation/lexigram/api/#dynamicmodule' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>DynamicModule</a> descriptor.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>stub</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>cls</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>config</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillsconfig' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/packages/foundation/lexigram/api/#dynamicmodule' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>DynamicModule</a></span></pre></div>

Create a SkillsModule suitable for unit and integration testing.

Uses in-memory or no-op skill implementations with minimal side
effects. Built-in skill registration is disabled by default to keep
the test container lightweight.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`config`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillsconfig' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional <a href='/platform/lexigram-ai-skills/api/#skillsconfig' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsConfig</a> override. Uses safe test defaults when ``None``.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/foundation/lexigram/api/#dynamicmodule' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>DynamicModule</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A <a href='/packages/foundation/lexigram/api/#dynamicmodule' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>DynamicModule</a> descriptor.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillsProvider`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Register and bootstrap the skills subsystem.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>config</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/platform/lexigram-ai-skills/api/#skillsconfig' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>enable_tool_bridge</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>bool</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>False</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise the provider with optional configuration.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`config`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skillsconfig' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillsConfig</a> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Skills configuration. Defaults to ``SkillsConfig()``.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`enable_tool_bridge`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>bool</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Register the tool-bridge adapter so agent tool registries can invoke skills as first-class tools. **kwargs: Reserved for future keyword arguments.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>register</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>container</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/foundation/lexigram-contracts/api/#containerregistrarprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ContainerRegistrarProtocol</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Register all skills services into the container.

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>boot</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>container</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/foundation/lexigram-contracts/api/#containerresolverprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ContainerResolverProtocol</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Register built-in and auto-discovered skills into the registry.

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>shutdown</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Perform any cleanup on shutdown (no-op for the skills provider).

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>health_check</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>timeout</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>5.0</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>HealthCheckResult</span></pre></div>

Health check — always healthy (in-process domain provider).

No external backend to ping.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`timeout`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>float</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ignored for in-process providers.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>HealthCheckResult</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Always HEALTHY — no external backend to ping.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `TextSummarizeSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Return a simple extractive summary of the provided text.

This built-in provides a deterministic word-count truncation summary.
For production use, replace or extend with an LLM-backed implementation.

Example output

```python
{"summary": "First 50 words of the input...", "word_count": 200}
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the text_summarize skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Summarise *text* by truncating to *max_words*.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok result with ``summary`` and ``word_count`` keys.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `TextTranslateSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Stub skill that echoes text with a language annotation.

Replace with an LLM or translation API backend for real translations.

Example output

```python
{"translated": "...", "source_language": "auto", "target_language": "es"}
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the text_translate skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Return the input text unchanged with metadata (stub).



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok result with ``translated``, ``source_language``, and ``target_language`` keys.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `ToolSkillAdapter`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Adapts a ``ToolProtocol`` into a ``SkillProtocol``.

Allows existing tool-based registries to participate in the skill
system without modification.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>tool</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/foundation/lexigram-contracts/api/#toolprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ToolProtocol</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Wrap *tool* as a skill.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`tool`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/foundation/lexigram-contracts/api/#toolprotocol' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>ToolProtocol</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>ToolProtocol-compliant object with name, description, parameters_schema, and execute() method.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the adapted skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition derived from the wrapped tool.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Delegate to the wrapped tool's execute method.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Result wrapping SkillResult on success or SkillError on failure.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>validate</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Tools have no built-in validation — always returns empty list.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ignored.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Empty list.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `WebSearchSkill`

</div>

<span data-api-type='Classes' style='display:none;'></span>


Search the web and return result snippets.

This is a stub implementation.  Integrate a real search API
(e.g. Brave, Bing, SerpAPI) by overriding execute.

Example output

```python
{
  "query": "AI trends 2026",
  "results": [],
  "stub": true
}
```


<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>definition</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></span></pre></div>

Return the skill definition.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/platform/lexigram-ai-skills/api/#skilldefinition' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillDefinition</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>SkillDefinition for the web_search skill.</td></tr></tbody></table></div>



<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Return an empty result set (stub).



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Result<span style='color: var(--lex-color-colon)'>[</span><a href='/platform/lexigram-ai-skills/api/#skillresult' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillResult</a><span style='color: var(--lex-color-colon)'>,</span> <a href='/platform/lexigram-ai-skills/api/#skillerror' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>SkillError</a><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Ok stub result with empty ``results`` list and ``stub=True``.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

## Functions


<div data-pagefind-weight='10'>

### `skill`

</div>

<span data-api-type='Functions' style='display:none;'></span>

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.9em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>skill</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>description</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>*</span><span style='color: var(--lex-color-name)'></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>category</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'general'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>cacheable</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>bool</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>False</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>max_retries</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>int</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>0</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>timeout_seconds</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>30.0</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>requires_confirmation</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>bool</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>False</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>permissions</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Callable</span></pre></div>

Convert an async function into a <a href='/platform/lexigram-ai-skills/api/#functionskill' style='color:inherit; text-decoration:underline; text-decoration-color:rgba(128,128,128,0.3); text-underline-offset:2px;'>FunctionSkill</a>.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Unique skill name.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`description`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>What the skill does.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`category`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Logical grouping for the skill.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`cacheable`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>bool</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Whether results can be cached.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`max_retries`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Retry attempts on failure (0 = no retry).</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`timeout_seconds`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>float</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Execution timeout.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`requires_confirmation`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>bool</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>If True, consumers may prompt for confirmation.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`permissions`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Required permission strings.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Callable</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Decorator that wraps the function as a FunctionSkill.</td></tr></tbody></table></div>



<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `skill_param`

</div>

<span data-api-type='Functions' style='display:none;'></span>

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.9em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>skill_param</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>*</span><span style='color: var(--lex-color-name)'></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>type</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'string'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>description</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>''</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>required</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>bool</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>True</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>default</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>enum</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>Any<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>min_value</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>max_value</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>max_length</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>int <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>Callable</span></pre></div>

Declare a parameter on a skill function.

Must be applied before ``@skill``.  Multiple ``@skill_param`` decorators
are accumulated in declaration order.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameter name.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`type`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>JSON Schema type (e.g. ``"string"``, ``"integer"``, ``"boolean"``).</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`description`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Human-readable description.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`required`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>bool</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Whether the parameter is required.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`default`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Default value when not supplied.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`enum`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>Any<span style='color: var(--lex-color-colon)'>]</span> <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Restricted set of allowed values.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`min_value`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>float <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Numeric minimum.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`max_value`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>float <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Numeric maximum.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`max_length`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>String maximum length.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Callable</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Decorator that annotates the function with parameter metadata.</td></tr></tbody></table></div>



<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `validate_non_empty_string`

</div>

<span data-api-type='Functions' style='display:none;'></span>

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.9em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>validate_non_empty_string</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>value</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Validate that *value* is a non-empty string.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`value`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Value to check.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameter name for error messages.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of validation errors.</td></tr></tbody></table></div>



<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `validate_params`

</div>

<span data-api-type='Functions' style='display:none;'></span>

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.9em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>validate_params</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>params</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>schema</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Validate *params* against a JSON Schema ``object`` descriptor.

Supports: required fields, type checking, enum, minimum/maximum,
minLength/maxLength, and nested object/array types.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`params`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The parameter dict supplied by the caller.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`schema`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>dict<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>JSON Schema ``object`` definition from SkillDefinition.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of validation error messages.  Empty list means valid.</td></tr></tbody></table></div>



<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `validate_positive_int`

</div>

<span data-api-type='Functions' style='display:none;'></span>

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.9em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>validate_positive_int</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>value</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Validate that *value* is a positive integer.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`value`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Value to check.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameter name for error messages.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of validation errors.</td></tr></tbody></table></div>



<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `validate_range`

</div>

<span data-api-type='Functions' style='display:none;'></span>

<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.9em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>validate_range</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>value</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>*</span><span style='color: var(--lex-color-name)'></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>minimum</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>maximum</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

Validate that *value* falls within a numeric range.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`value`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Value to check.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Parameter name for error messages.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`minimum`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>float <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Inclusive lower bound.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`maximum`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>float <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Inclusive upper bound.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of validation errors.</td></tr></tbody></table></div>



<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

## Exceptions


<div data-pagefind-weight='10'>

### `SkillAlreadyRegisteredError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>


Raised when a skill is registered under a name that already exists.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with the duplicate skill name.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill that was already registered.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>


Base for skill execution errors.

Extended in lexigram-ai-skills with specific failures like
skill not found, execution failure, parameter validation, etc.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'Skill error'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillExecutionError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>


Raised when a skill execution fails after all retry attempts.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>cause</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Exception <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with an error message and optional cause.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`message`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Human-readable error description.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`cause`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Exception <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The underlying exception, if any.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill that failed (optional).</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillNotFoundError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>


Raised when a requested skill is not registered.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with the missing skill name.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill that was not found.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillPermissionDeniedError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>


Raised when the caller lacks required permissions for a skill.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>required</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with permission details.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill that requires permissions.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`required`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Required permission strings.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillRoutingError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>


Raised when a SkillRouter finds no matching route.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'No matching route'</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with an optional detail message.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`message`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Human-readable description of the routing failure.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillTimeoutError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>


Raised when skill execution exceeds the configured timeout.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>timeout_seconds</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with timeout context.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill that timed out.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`timeout_seconds`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>float</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The timeout that was exceeded.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SkillValidationError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>


Raised when skill parameter validation fails.

<div style='padding-left: 1rem; border-left: 1px solid var(--sl-color-gray-5); margin-top: 2rem; margin-bottom: 2rem;'>
<div style='background: var(--color-background-weak); padding: 0.6rem 1rem; border-radius: 4px; border-left: 2px solid var(--color-border-weak); margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: flex-start;'><pre style='margin: 0; font-family: var(--sl-font-mono); font-size: 0.875em; line-height: 1.6; white-space: pre-wrap; word-break: break-all; flex: 1;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>skill_name</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>errors</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

Initialise with validation error details.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`skill_name`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Name of the skill that failed validation.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`errors`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>str<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of human-readable validation error messages.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:2px solid rgba(99,102,241,0.45);margin:1.75rem 0 0 0;' />
