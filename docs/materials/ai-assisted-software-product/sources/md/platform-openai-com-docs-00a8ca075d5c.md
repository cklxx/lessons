# Overview | OpenAI Platform

- URL: https://platform.openai.com/docs/
- Retrieved: 2025-12-17T16:09:41.009759+00:00

[](/docs/overview)
[DocsDocs](/docs)[API referenceAPI](/docs/api-reference/introduction)
Log in[Sign up](/signup)
Search
Get started
[Overview](/docs/overview)
[Quickstart](/docs/quickstart)
[Models](/docs/models)
[Pricing](/docs/pricing)
[Libraries](/docs/libraries)
[Latest: GPT-5.2](/docs/guides/latest-model)
Core concepts
[Text generation](/docs/guides/text)
[Code generation](/docs/guides/code-generation)
[Images and vision](/docs/guides/images-vision)
[Audio and speech](/docs/guides/audio)
[Structured output](/docs/guides/structured-outputs)
[Function calling](/docs/guides/function-calling)
[Responses API](/docs/guides/migrate-to-responses)
Agents
[Overview](/docs/guides/agents)
Build agents
Deploy in your product
Optimize
[Voice agents](/docs/guides/voice-agents)
Tools
[Using tools](/docs/guides/tools)
[Connectors and MCP](/docs/guides/tools-connectors-mcp)
[Web search](/docs/guides/tools-web-search)
[Code interpreter](/docs/guides/tools-code-interpreter)
File search and retrieval
More tools
Run and scale
[Conversation state](/docs/guides/conversation-state)
[Background mode](/docs/guides/background)
[Streaming](/docs/guides/streaming-responses)
[Webhooks](/docs/guides/webhooks)
[File inputs](/docs/guides/pdf-files)
Prompting
Reasoning
Evaluation
[Getting started](/docs/guides/evaluation-getting-started)
[Working with evals](/docs/guides/evals)
[Prompt optimizer](/docs/guides/prompt-optimizer)
[External models](/docs/guides/external-models)
[Best practices](/docs/guides/evaluation-best-practices)
Realtime API
[Overview](/docs/guides/realtime)
Connect
Usage
Model optimization
[Optimization cycle](/docs/guides/model-optimization)
Fine-tuning
[Graders](/docs/guides/graders)
Specialized models
[Image generation](/docs/guides/image-generation)
[Video generation](/docs/guides/video-generation)
[Text to speech](/docs/guides/text-to-speech)
[Speech to text](/docs/guides/speech-to-text)
[Deep research](/docs/guides/deep-research)
[Embeddings](/docs/guides/embeddings)
[Moderation](/docs/guides/moderation)
Coding agents
[Codex cloud](https://developers.openai.com/codex/cloud)
[Agent internet access](https://developers.openai.com/codex/cloud/agent-internet)
[Codex CLI](https://developers.openai.com/codex/cli)
[Codex IDE](https://developers.openai.com/codex/ide)
[Codex changelog](https://developers.openai.com/codex/changelog)
Going live
[Production best practices](/docs/guides/production-best-practices)
Latency optimization
Cost optimization
[Accuracy optimization](/docs/guides/optimizing-llm-accuracy)
Safety
Specialized APIs
Assistants API
Resources
[Terms and policies](https://openai.com/policies)
[Changelog](/docs/changelog)
[Your data](/docs/guides/your-data)
[Permissions](/docs/guides/rbac)
[Rate limits](/docs/guides/rate-limits)
[Deprecations](/docs/deprecations)
[MCP for deep research](/docs/mcp)
[Developer mode](/docs/guides/developer-mode)
ChatGPT Actions
# OpenAI Platform
## Developer quickstart
Make your first API request in minutes. Learn the basics of the OpenAI platform.
[Get started](/docs/quickstart)
javascript
    
    1
    2
    3
    4
    5
    6
    7
    curl https://api.openai.com/v1/responses \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "model": "gpt-5.2",
        "input": "Write a short bedtime story about a unicorn."
      }'
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    import OpenAI from "openai";
    const client = new OpenAI();
    
    const response = await client.responses.create({
      model: "gpt-5.2",
      input: "Write a short bedtime story about a unicorn.",
    });
    
    console.log(response.output_text);
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    from openai import OpenAI
    client = OpenAI()
    
    response = client.responses.create(
        model="gpt-5.2",
        input="Write a short bedtime story about a unicorn."
    )
    
    print(response.output_text)
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    using OpenAI.Responses;
    
    string apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
    var client = new OpenAIResponseClient(model: "gpt-5.2", apiKey: apiKey);
    
    OpenAIResponse response = client.CreateResponse(
        "Write a short bedtime story about a unicorn."
    );
    
    Console.WriteLine(response.GetOutputText());
Models
[View all](/docs/models)
[GPT-5.2NewThe best model for coding and agentic tasks across industries](/docs/models/gpt-5.2)[GPT-5 miniA faster, cost-efficient version of GPT-5 for well-defined tasks](/docs/models/gpt-5-mini)[GPT-5 nanoFastest, most cost-efficient version of GPT-5](/docs/models/gpt-5-nano)
## 
Start building
[Read and generate textUse the API to prompt a model and generate text](/docs/guides/text)[Use a model's vision capabilitiesAllow models to see and analyze images in your application](/docs/guides/images)[Generate images as outputCreate images with GPT Image 1](/docs/guides/image-generation)[Build apps with audioAnalyze, transcribe, and generate audio with API endpoints](/docs/guides/audio)[Build agentic applicationsUse the API to build agents that use tools and computers](/docs/guides/agents)[Achieve complex tasks with reasoningUse reasoning models to carry out complex tasks](/docs/guides/reasoning)[Get structured data from modelsUse Structured Outputs to get model responses that adhere to a JSON schema](/docs/guides/structured-outputs)[Tailor to your use caseAdjust our models to perform specifically for your use case with fine-tuning, evals, and distillation](/docs/guides/fine-tuning)
[Help centerFrequently asked account and billing questions](https://help.openai.com)[Developer forumDiscuss topics with other developers](https://community.openai.com/)[CookbookOpen-source collection of examples and guides](https://cookbook.openai.com/)[StatusCheck the status of OpenAI services](https://status.openai.com)
