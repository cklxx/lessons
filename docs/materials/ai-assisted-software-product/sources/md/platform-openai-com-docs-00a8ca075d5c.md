# Overview | OpenAI Platform

- URL: https://platform.openai.com/docs/
- Retrieved: 2025-12-17T16:09:41.009759+00:00

(/docs/overview)
[DocsDocs](https://platform.openai.com/docs)[API referenceAPI](https://platform.openai.com/docs/api-reference/introduction)
Log in[Sign up](https://platform.openai.com/signup)
Search
Get started
[Overview](https://platform.openai.com/docs/overview)
[Quickstart](https://platform.openai.com/docs/quickstart)
[Models](https://platform.openai.com/docs/models)
[Pricing](https://platform.openai.com/docs/pricing)
[Libraries](https://platform.openai.com/docs/libraries)
[Latest: GPT-5.2](https://platform.openai.com/docs/guides/latest-model)
Core concepts
[Text generation](https://platform.openai.com/docs/guides/text)
[Code generation](https://platform.openai.com/docs/guides/code-generation)
[Images and vision](https://platform.openai.com/docs/guides/images-vision)
[Audio and speech](https://platform.openai.com/docs/guides/audio)
[Structured output](https://platform.openai.com/docs/guides/structured-outputs)
[Function calling](https://platform.openai.com/docs/guides/function-calling)
[Responses API](https://platform.openai.com/docs/guides/migrate-to-responses)
Agents
[Overview](https://platform.openai.com/docs/guides/agents)
Build agents
Deploy in your product
Optimize
[Voice agents](https://platform.openai.com/docs/guides/voice-agents)
Tools
[Using tools](https://platform.openai.com/docs/guides/tools)
[Connectors and MCP](https://platform.openai.com/docs/guides/tools-connectors-mcp)
[Web search](https://platform.openai.com/docs/guides/tools-web-search)
[Code interpreter](https://platform.openai.com/docs/guides/tools-code-interpreter)
File search and retrieval
More tools
Run and scale
[Conversation state](https://platform.openai.com/docs/guides/conversation-state)
[Background mode](https://platform.openai.com/docs/guides/background)
[Streaming](https://platform.openai.com/docs/guides/streaming-responses)
[Webhooks](https://platform.openai.com/docs/guides/webhooks)
[File inputs](https://platform.openai.com/docs/guides/pdf-files)
Prompting
Reasoning
Evaluation
[Getting started](https://platform.openai.com/docs/guides/evaluation-getting-started)
[Working with evals](https://platform.openai.com/docs/guides/evals)
[Prompt optimizer](https://platform.openai.com/docs/guides/prompt-optimizer)
[External models](https://platform.openai.com/docs/guides/external-models)
[Best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)
Realtime API
[Overview](https://platform.openai.com/docs/guides/realtime)
Connect
Usage
Model optimization
[Optimization cycle](https://platform.openai.com/docs/guides/model-optimization)
Fine-tuning
[Graders](https://platform.openai.com/docs/guides/graders)
Specialized models
[Image generation](https://platform.openai.com/docs/guides/image-generation)
[Video generation](https://platform.openai.com/docs/guides/video-generation)
[Text to speech](https://platform.openai.com/docs/guides/text-to-speech)
[Speech to text](https://platform.openai.com/docs/guides/speech-to-text)
[Deep research](https://platform.openai.com/docs/guides/deep-research)
[Embeddings](https://platform.openai.com/docs/guides/embeddings)
[Moderation](https://platform.openai.com/docs/guides/moderation)
Coding agents
[Codex cloud](https://developers.openai.com/codex/cloud)
[Agent internet access](https://developers.openai.com/codex/cloud/agent-internet)
[Codex CLI](https://developers.openai.com/codex/cli)
[Codex IDE](https://developers.openai.com/codex/ide)
[Codex changelog](https://developers.openai.com/codex/changelog)
Going live
[Production best practices](https://platform.openai.com/docs/guides/production-best-practices)
Latency optimization
Cost optimization
[Accuracy optimization](https://platform.openai.com/docs/guides/optimizing-llm-accuracy)
Safety
Specialized APIs
Assistants API
Resources
[Terms and policies](https://openai.com/policies)
[Changelog](https://platform.openai.com/docs/changelog)
[Your data](https://platform.openai.com/docs/guides/your-data)
[Permissions](https://platform.openai.com/docs/guides/rbac)
[Rate limits](https://platform.openai.com/docs/guides/rate-limits)
[Deprecations](https://platform.openai.com/docs/deprecations)
[MCP for deep research](https://platform.openai.com/docs/mcp)
[Developer mode](https://platform.openai.com/docs/guides/developer-mode)
ChatGPT Actions
# OpenAI Platform
## Developer quickstart
Make your first API request in minutes. Learn the basics of the OpenAI platform.
[Get started](https://platform.openai.com/docs/quickstart)
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
[View all](https://platform.openai.com/docs/models)
[GPT-5.2NewThe best model for coding and agentic tasks across industries](https://platform.openai.com/docs/models/gpt-5.2)[GPT-5 miniA faster, cost-efficient version of GPT-5 for well-defined tasks](https://platform.openai.com/docs/models/gpt-5-mini)[GPT-5 nanoFastest, most cost-efficient version of GPT-5](https://platform.openai.com/docs/models/gpt-5-nano)
## 
Start building
[Read and generate textUse the API to prompt a model and generate text](https://platform.openai.com/docs/guides/text)[Use a model's vision capabilitiesAllow models to see and analyze images in your application](https://platform.openai.com/docs/guides/images)[Generate images as outputCreate images with GPT Image 1](https://platform.openai.com/docs/guides/image-generation)[Build apps with audioAnalyze, transcribe, and generate audio with API endpoints](https://platform.openai.com/docs/guides/audio)[Build agentic applicationsUse the API to build agents that use tools and computers](https://platform.openai.com/docs/guides/agents)[Achieve complex tasks with reasoningUse reasoning models to carry out complex tasks](https://platform.openai.com/docs/guides/reasoning)[Get structured data from modelsUse Structured Outputs to get model responses that adhere to a JSON schema](https://platform.openai.com/docs/guides/structured-outputs)[Tailor to your use caseAdjust our models to perform specifically for your use case with fine-tuning, evals, and distillation](https://platform.openai.com/docs/guides/fine-tuning)
[Help centerFrequently asked account and billing questions](https://help.openai.com)[Developer forumDiscuss topics with other developers](https://community.openai.com/)[CookbookOpen-source collection of examples and guides](https://cookbook.openai.com/)[StatusCheck the status of OpenAI services](https://status.openai.com)
