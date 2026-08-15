---
title: API Reference
description: Complete API reference for the lexigram-queue package.
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

### `QueueProtocol`

</div>

<span data-api-type='Protocols' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/protocols.py#L16' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Structural protocol for message queue / bus backends.

Implementations include in-memory, Redis Pub/Sub, RabbitMQ, Kafka,
and SQS.  ``connect()`` / ``close()`` manage the connection lifecycle;
``publish()`` and ``subscribe()`` handle message delivery.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>connect</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>connect</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/protocols.py#L24' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Establish connection to the broker.

<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>close</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>close</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/protocols.py#L28' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Close the connection and release resources.

<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>publish</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>publish</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>topic</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/protocols.py#L32' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Publish a message to a topic.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`topic`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Destination topic or queue name.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`message`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The message to publish.</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Raises</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Exception</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#queueerror' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>QueueError</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>For expected publish failures (quota, auth, etc.).</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>subscribe</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>subscribe</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>topic</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>handler</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Callable<span style='color: var(--lex-color-colon)'>[</span><span style='color: var(--lex-color-colon)'>[</span><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a><span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>,</span> Coroutine<span style='color: var(--lex-color-colon)'>[</span>Any<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>,</span> <span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/protocols.py#L44' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Subscribe a handler to a topic.

The handler is called for each message received.  The backend is
responsible for acknowledging or rejecting messages.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`topic`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Topic or queue name to subscribe to.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`handler`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Callable<span style='color: var(--lex-color-colon)'>[</span><span style='color: var(--lex-color-colon)'>[</span><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a><span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>,</span> Coroutine<span style='color: var(--lex-color-colon)'>[</span>Any<span style='color: var(--lex-color-colon)'>,</span> Any<span style='color: var(--lex-color-colon)'>,</span> <span style='color: var(--lex-color-default) !important'>None</span><span style='color: var(--lex-color-colon)'>]</span><span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Async callable invoked per message.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>health_check</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>health_check</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>timeout</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>float</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>5.0</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>HealthCheckResult</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/protocols.py#L60' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Check broker connectivity.
</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

## Classes


<div data-pagefind-weight='10'>

### `BusMessage`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/types.py#L28' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
A message transported through the queue backend.

``id`` defaults to a new UUID4.  ``timestamp`` defaults to the current
wall-clock time.  Both are set via field defaults so callers do not need
to supply them.

Attributes:
    id: Unique message identifier.
    topic: Destination topic or queue name.
    payload: Arbitrary message body; must be serialisable by the backend.
    headers: Opaque string key-value headers passed to the broker.
    timestamp: Unix epoch timestamp when the message was created.
    ttl: Time-to-live in seconds; ``None`` uses the backend default.
    priority: Message priority (higher = more urgent); backend-dependent.
    delivery_guarantee: Delivery semantics for this message.
    retry_count: Number of times this message has been retried.
    max_retries: Maximum retries before routing to DLQ.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>is_expired</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>is_expired</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>bool</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/types.py#L59' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Return ``True`` if the message TTL has elapsed.

<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>should_retry</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>should_retry</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>bool</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/types.py#L65' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Return ``True`` if the message may be retried.
</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `ConsumerRegisteredEvent`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/events.py#L42' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Consumer was registered to a queue.

Consumed by: consumer tracking, lifecycle management, monitoring.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `DeadLetterQueue`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/dlq.py#L27' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
In-memory dead letter queue for storing failed messages.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>max_size</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>int</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>1000</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/dlq.py#L30' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Initialize DLQ.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`max_size`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>int</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Maximum number of entries to store.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>push</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>push</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>error</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/dlq.py#L39' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Add a failed message to the DLQ.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`message`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The message that failed.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`error`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Error description.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>drain</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>drain</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>list<span style='color: var(--lex-color-colon)'>[</span>DeadLetterEntry<span style='color: var(--lex-color-colon)'>]</span></span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/dlq.py#L52' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Remove and return all entries from the DLQ.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>list<span style='color: var(--lex-color-colon)'>[</span>DeadLetterEntry<span style='color: var(--lex-color-colon)'>]</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>List of dead letter entries.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>size</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>property </span><span style='color: var(--lex-color-fname); font-weight: 600'>size</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>int</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/dlq.py#L62' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Return current number of entries in DLQ.
</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MessageConsumedEvent`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/events.py#L12' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Message was successfully consumed from the queue.

Consumed by: message tracking, audit logging, metrics collection.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MessageConsumedHook`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/hooks.py#L33' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Payload fired when a message is successfully consumed by a handler.

Attributes:
    queue_name: Name of the queue or topic the message came from.
    message_type: Type label of the consumed message.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MessageConsumer`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/consumers/consumer.py#L17' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Base class for message consumer workers.

Subclass this and implement handle() to create a worker that
subscribes to a topic and processes incoming messages.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>queue</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#queueprotocol' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>QueueProtocol</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/consumers/consumer.py#L26' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Initialize consumer.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`queue`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#queueprotocol' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>QueueProtocol</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Queue protocol instance for subscribing.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>start</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>start</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/consumers/consumer.py#L35' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Start consuming messages from the subscribed topic.

<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>stop</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>stop</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/consumers/consumer.py#L41' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Stop consuming messages.

<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>handle</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>handle</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/consumers/consumer.py#L60' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Handle a received message. Subclasses must implement this.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`message`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Message to handle.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MessageDeadLetteredEvent`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/events.py#L27' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Message failed and was moved to dead-letter queue.

Consumed by: error handling, retry management, incident tracking.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MessagePipeline`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/pipeline.py#L30' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Ordered chain of middleware around a terminal handler.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/pipeline.py#L33' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Initialize pipeline.

<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>add</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>add</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>middleware</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#middlewarebase' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>MiddlewareBase</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/pipeline.py#L37' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Add middleware to the pipeline.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`middleware`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#middlewarebase' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>MiddlewareBase</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Middleware instance to add.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>execute</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>execute</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>handler</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/pipeline.py#L45' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Execute the middleware chain and terminal handler.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`message`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The message to process.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`handler`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Terminal async callable to invoke after all middleware.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MessagePublishedHook`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/hooks.py#L20' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Payload fired when a message is published to a queue or topic.

Attributes:
    queue_name: Name of the queue or topic the message was published to.
    message_type: Type label of the published message.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `MiddlewareBase`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/pipeline.py#L16' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Base class for message pipeline middleware.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>process</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>process</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>next_handler</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/pipeline.py#L20' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Process a message and pass to the next handler.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`message`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>The message to process.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`next_handler`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>Any</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Async callable to invoke the next middleware or terminal handler.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `QueueDrainedHook`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/hooks.py#L46' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Payload fired when a queue is fully drained (all pending messages processed).

Attributes:
    queue_name: Name of the queue that was drained.

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `QueueModule`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/module.py#L15' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Message queue/bus integration with Named DI multi-backend support.

Registers <a href='/packages/events/lexigram-queue/api/#queueprotocol' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>QueueProtocol</a> for
constructor injection.

Usage

```python
from lexigram.queue.config import QueueConfig, NamedQueueConfig
from lexigram.queue.module import QueueModule

@module(
    imports=[QueueModule.configure(QueueConfig(backends=[...]))]
)
class AppModule(Module):
    pass
```


    from lexigram.queue.config import QueueConfig, NamedQueueConfig
    from lexigram.queue.module import QueueModule

    @module(
        imports=[QueueModule.configure(QueueConfig(backends=[...]))]
    )
    class AppModule(Module):
        pass

Scope consumers into a feature module

```python
@module(
    imports=[
        QueueModule.configure(QueueConfig(...)),
        QueueModule.scope(OrderConsumer, PaymentConsumer),
    ]
)
class OrdersFeatureModule(Module):
    pass
```


    @module(
        imports=[
            QueueModule.configure(QueueConfig(...)),
            QueueModule.scope(OrderConsumer, PaymentConsumer),
        ]
    )
    class OrdersFeatureModule(Module):
        pass

Named injection

```python
class MyService:
    def __init__(
        self,
        queue: QueueProtocol,                                   # primary
        events: Annotated[QueueProtocol, Named("events")],     # named
    ) -> None: ...
```


    class MyService:
        def __init__(
            self,
            queue: QueueProtocol,                                   # primary
            events: Annotated[QueueProtocol, Named("events")],     # named
        ) -> None: ...

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>configure</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>configure</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>cls</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>config</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>QueueConfig <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> Any <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>DynamicModule</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/module.py#L54' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Create a QueueModule with explicit configuration.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`config`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>QueueConfig <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> Any <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>QueueConfig or ``None`` to use defaults (reads from environment variables).</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>DynamicModule</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A DynamicModule descriptor.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>scope</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>scope</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>cls</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>*</span><span style='color: var(--lex-color-name)'>consumers</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>type</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>DynamicModule</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/module.py#L86' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Scope queue consumer classes into a feature module.

Registers the given consumer classes as providers so they are
discovered and wired by the queue backend.  The parent module graph
must already include <a href='/packages/events/lexigram-queue/api/#queuemodule' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>QueueModule</a>.configure — this does
**not** create a new queue connection.

Uses the anonymous token pattern so both ``configure()`` and
``scope()`` can coexist in the same compiled graph without a
``ModuleDuplicateError``.

Example

```python
@module(
    imports=[
        QueueModule.configure(QueueConfig(...)),
        QueueModule.scope(OrderConsumer, PaymentConsumer),
    ]
)
class OrdersFeatureModule(Module):
    pass
```


    @module(
        imports=[
            QueueModule.configure(QueueConfig(...)),
            QueueModule.scope(OrderConsumer, PaymentConsumer),
        ]
    )
    class OrdersFeatureModule(Module):
        pass



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>DynamicModule</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A DynamicModule scoped to this feature.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>stub</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>stub</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>cls</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>config</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>QueueConfig <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-default) !important'>None</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-return)'>DynamicModule</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/module.py#L127' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Return an in-memory QueueModule for unit testing.

Uses a memory backend so no external broker is required.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`config`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>QueueConfig <span style='color: var(--lex-color-colon)'><span style='color: var(--lex-color-colon)'>|</span></span> <span style='color: var(--lex-color-default) !important'>None</span></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Optional config override; defaults to empty QueueConfig (which uses memory backend).</td></tr></tbody></table></div>




<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Returns</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:45%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>DynamicModule</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>A DynamicModule descriptor.</td></tr></tbody></table></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `TransactionalOutbox`

</div>

<span data-api-type='Classes' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/outbox.py#L27' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Stage messages within a transaction, flush atomically.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-name)'>queue</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#queueprotocol' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>QueueProtocol</a></span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/outbox.py#L30' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Initialize outbox.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`queue`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#queueprotocol' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>QueueProtocol</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Queue protocol to publish messages to.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>stage</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>stage</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>topic</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/outbox.py#L39' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Stage a message for publish within a transaction.



<div style='margin:0;line-height:1.4;'><span style='display:block;font-size:0.7em;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-brand);margin-top:1rem;margin-bottom:0.4rem;'>Parameters</span><table style='border-collapse:collapse;width:100%;font-size:0.85em;margin:0;margin-bottom:1rem;table-layout:fixed;'><thead><tr><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:20%;'>Parameter</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);width:25%;'>Type</th><th style='text-align:left;padding:0.4rem 0.5rem;color:var(--color-text-strong);font-weight:600;font-size:0.82em;border-bottom:1px solid var(--color-border-weak);padding-left:1.2rem;border-left:1px solid var(--color-border-weak);width:55%;'>Description</th></tr></thead><tbody><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`topic`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'>str</td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Destination topic.</td></tr><tr><td style='padding:0.6rem 0.5rem;vertical-align:top;white-space:nowrap;font-family:var(--sl-font-mono);font-size:0.85em;color:var(--lex-color-name);border-bottom:1px solid var(--color-border-weak);'>`message`</td><td style='padding:0.6rem 0.5rem;vertical-align:top;color:var(--lex-color-type) !important;font-family:var(--sl-font-mono);font-size:0.82em;border-bottom:1px solid var(--color-border-weak);'><a href='/packages/events/lexigram-queue/api/#busmessage' style='color:inherit;text-decoration:underline;text-decoration-color:rgba(128,128,128,0.3);text-underline-offset:2px;'>BusMessage</a></td><td style='padding:0.6rem 0.5rem 0.6rem 1.2rem;vertical-align:top;font-size:0.9em;font-family:var(--sl-font-mono);color:var(--color-text-weak);border-left:1px solid var(--color-border-weak);border-bottom:1px solid var(--color-border-weak);'>Message to stage.</td></tr></tbody></table></div>



<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>flush</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>async </span><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>flush</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/outbox.py#L48' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Publish all staged messages that haven't been published yet.

<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>clear</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>clear</span><span style='color: var(--lex-color-colon)'>(</span><span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/core/outbox.py#L67' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>

Clear all staged entries.
</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

## Exceptions


<div data-pagefind-weight='10'>

### `AzureServiceBusQueueError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L46' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Azure Service Bus queue failure.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'Azure Service Bus error'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L51' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `GCPPubSubQueueError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L55' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
GCP Pub/Sub queue failure.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'GCP Pub/Sub error'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L60' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `KafkaQueueError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L28' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Kafka queue failure.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'Kafka error'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L33' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `QueueError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/errors.py#L11' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Base for expected, recoverable queue / bus failures.

Attributes:
    backend: Name of the queue backend (e.g. "redis", "kafka").
    topic: Topic or queue name where the failure occurred.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'Queue error'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>*</span><span style='color: var(--lex-color-name)'></span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>backend</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'unknown'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-name)'>topic</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'unknown'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-contracts/src/lexigram/contracts/queue/errors.py#L21' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `RabbitMQQueueError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L19' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
RabbitMQ queue failure.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'RabbitMQ error'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L24' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `RedisQueueError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L10' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
Redis queue failure.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'Redis queue error'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L15' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />

<div data-pagefind-weight='10'>

### `SQSQueueError`

</div>

<span data-api-type='Exceptions' style='display:none;'></span>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L37' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.75rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='14' height='14' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>
SQS queue failure.

<div style='padding-left:1rem;border-left:1px solid var(--sl-color-gray-5);margin-top:2rem;margin-bottom:2rem;'>
<div style='border-radius:8px;border:1px solid var(--color-border-weak);overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.35);margin-bottom:1rem;'><div style='background:var(--color-background-weak);border-bottom:1px solid var(--color-border-weak);padding:0 1rem;min-height:36px;display:flex;align-items:center;padding-left:70px;position:relative;'><span style='position:absolute;top:50%;left:16px;transform:translateY(-50%);display:inline-block;width:12px;height:12px;border-radius:50%;background-color:#ff5f56;box-shadow:20px 0 0 #ffbd2e,40px 0 0 #27c93f;'></span><span style='font-family:var(--sl-font-mono);font-size:0.72em;color:var(--color-text-weaker);'>__init__</span></div><pre style='margin:0;background:var(--color-background-weak);font-family:var(--sl-font-mono);font-size:0.875em;line-height:1.65;white-space:pre-wrap;word-break:break-all;padding:0.75rem 1rem;'><span style='color: var(--lex-color-keyword)'>def </span><span style='color: var(--lex-color-fname); font-weight: 600'>__init__</span><span style='color: var(--lex-color-colon)'>(</span>
    <span style='color: var(--lex-color-name)'>message</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>str</span><span style='color: var(--lex-color-colon)'> = </span><span style='color: var(--lex-color-string) !important'>'SQS error'</span><span style='color: var(--lex-color-colon)'>,</span>
    <span style='color: var(--lex-color-default) !important'>**</span><span style='color: var(--lex-color-name)'>kwargs</span><span style='color: var(--lex-color-colon)'>: </span><span style='color: var(--lex-color-type)'>Any</span>
<span style='color: var(--lex-color-colon)'>)</span><span style='color: var(--lex-color-keyword)'> -> </span><span style='color: var(--lex-color-default) !important'>None</span></pre></div>

<div style='display:flex;justify-content:flex-end;margin-top:-0.5rem;margin-bottom:0.5rem;'><a href='https://github.com/dbtinoy-/lexigram/blob/main/lexigram-queue/src/lexigram/queue/exceptions.py#L42' target='_blank' rel='noopener noreferrer' style='display:inline-flex;align-items:center;gap:0.3rem;font-size:0.7rem;color:var(--sl-color-gray-3);text-decoration:none;'><svg viewBox='0 0 16 16' width='12' height='12' fill='currentColor'><path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/></svg>source</a></div>


</div>

<hr style='border:none;border-top:1px solid rgba(200,255,0,0.2);margin:1.75rem 0 0 0;' />
