# KServe

- URL: https://kserve.github.io/website/
- Retrieved: 2025-12-17T17:03:43.771320+00:00

[Skip to main content](#__docusaurus_skipToContent_fallback)
🎉️ **[KServe has joined CNCF!](https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/)** 🥳️
[**KServe**](/website/)[Docs](/website/docs/intro)[Blog](/website/blog)
[0.16](/website/docs/intro)
  * [nightly](/website/docs/next/intro)
  * [0.16](/website/docs/intro)
  * [0.15](https://kserve.github.io/archive/0.15/)
  * [0.14 ](https://kserve.github.io/archive/0.14/)
  * [0.13](https://kserve.github.io/archive/0.13/)
  * [0.12](https://kserve.github.io/archive/0.12/)
  * [0.11](https://kserve.github.io/archive/0.11/)


[Community](/website/docs/community/get-involved)[](https://github.com/kserve/kserve)
# KServe
Standardized Distributed Generative and Predictive AI Inference Platform for Scalable, Multi-Framework Deployment on Kubernetes
[Get Started](/website/docs/getting-started/genai-first-isvc)[Install KServe](/website/docs/admin-guide/overview#installation)
## Why KServe?
The open-source standard for self-hosted AI, providing a unified platform for both Generative and Predictive AI inference on Kubernetes.Simple enough for quick deployments, yet powerful enough for the most demanding enterprise workloads.
### 🤖 Generative AI
#### 🧠 LLM-Optimized
OpenAI-compatible inference protocol for seamless integration with large language models
#### 🚅 GPU Acceleration
High-performance serving with GPU support and optimized memory management for large models
#### 💾 Model Caching
Intelligent model caching to reduce loading times and improve response latency for frequently used models
#### 🗂️ KV Cache Offloading
Advanced memory management with KV cache offloading to CPU/disk for handling longer sequences efficiently
#### 📈 Autoscaling
Request-based autoscaling capabilities optimized for generative workload patterns
#### 🔧 Hugging Face Ready
Native support for Hugging Face models with streamlined deployment workflows
### 📊 Predictive AI
#### 🧮 Multi-Framework
Support for TensorFlow, PyTorch, scikit-learn, XGBoost, ONNX, and more
#### 🔀 Intelligent Routing
Seamless request routing between predictor, transformer, and explainer components with automatic traffic management
#### 🔄 Advanced Deployments
Canary rollouts, inference pipelines, and ensembles with InferenceGraph
#### ⚡ Auto-scaling
Request-based autoscaling with scale-to-zero for predictive workloads
#### 🔍 Model Explainability
Built-in support for model explanations and feature attribution to understand prediction reasoning
#### 📊 Advanced Monitoring
Enables payload logging, outlier detection, adversarial detection, and drift detection with AI Fairness 360 and ART integration
#### 💰 Cost Efficient
Scale-to-zero on expensive resources when not in use, reducing infrastructure costs
## Simple and Powerful API
KServe provides a Kubernetes Custom Resource Definition for serving predictive and generative machine learning models. It encapsulates the complexity of autoscaling, networking, health checking, and server configuration to bring cutting edge serving features to your ML deployments.
✓Standard K8s API across ML frameworks
✓Pre/post processing and explainability
✓OpenAI specification support for LLMs
✓Canary rollouts and A/B testing
    
    apiVersion: "serving.kserve.io/v1beta1"  
    kind: "InferenceService"  
    metadata:  
      name: "llm-service"  
    spec:  
      predictor:  
        model:  
          modelFormat:  
            name: huggingface  
          resources:  
            limits:  
              cpu: "6"  
              memory: 24Gi  
              nvidia.com/gpu: "1"  
          storageUri: "hf://meta-llama/Llama-3.1-8B-Instruct"  
    
## How KServe Works
KServe provides a Kubernetes custom resource definition for serving ML models on arbitrary frameworks, encapsulating complexity of autoscaling, networking, health checking, and server configuration to bring cutting edge serving features to your ML deployments.
### Control Plane
Manages lifecycle of ML models, providing model revision tracking, canary rollouts, and A/B testing
### Data Plane
Standardized inference protocol for model servers with request/response APIs, supporting both predictive and generative models
### InferenceService
Core Kubernetes custom resource that simplifies ML model deployment with automatic scaling, networking, and health checks
### Inference Graph
Enables advanced deployments with pipelines for pre/post processing, ensembles, and multi-model workflows
## Quick Start
Get started with KServe in minutes. Follow these simple steps to deploy your first model.
1
### Install KServe
Install KServe and its dependencies on your Kubernetes cluster:
    
    kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.0/kserve.yaml  
    
2
### Create an InferenceService
Deploy a pre-trained model with a simple YAML configuration:
    
    apiVersion: "serving.kserve.io/v1beta1"  
    kind: "InferenceService"  
    metadata:  
      name: "qwen-llm"  
    spec:  
      predictor:  
        model:  
          modelFormat:  
            name: huggingface  
          storageUri: "hf://Qwen/Qwen2.5-0.5B-Instruct"  
          resources:  
            requests:  
              cpu: "1"  
              memory: 4Gi  
              nvidia.com/gpu: "1"  
    
3
### Send Inference Requests
Make predictions using the deployed model:
    
    curl -v -H "Host: qwen-llm.default.example.com" \  
      http://localhost:8080/openai/v1/chat/completions -d @./prompt.json  
    
[Detailed Guide](/website/docs/getting-started/genai-first-isvc)
## Trusted by Industry Leaders
KServe is used in production by organizations across various industries, providing reliable model inference at scale.
[](https://www.bloomberg.com/)[](https://www.ibm.com/)[](https://www.redhat.com/)[](https://www.nvidia.com/)[](https://www.amd.com/)[](https://www.kubeflow.org/)[](https://www.cloudera.com/)[](https://canonical.com/)[](https://www.cisco.com/)[](https://www.gojek.com/)[](https://www.inspur.com/)[](https://www.maxkelsen.com/)[](https://www.prosus.com/)[](https://wikimediafoundation.org/)[](https://www.navercorp.com/)[](https://www.zillow.com/)[](https://striveworks.us/)[](https://www.cars24.com/)[](https://www.upstage.ai/)[](https://www.intuit.com/)[](https://www.alauda.io/)
[View all adopters →](/website/docs/community/adopters)
## Ready to Transform Your ML Deployment?
Simplify your journey from model development to production with KServe's standardized inference platform for both predictive and generative AI models
[Get Started](/website/docs/getting-started/genai-first-isvc)[Install KServe](/website/docs/admin-guide/overview#installation)
Documentation
  * [Get Started](/website/docs/getting-started/quickstart-guide)
  * [GenAI Model Serving Guide](/website/docs/model-serving/generative-inference/overview)
  * [Predictive AI Model Serving Guide](/website/docs/model-serving/predictive-inference/frameworks/overview)
  * [API Reference](/website/docs/reference/crd-api)


Community
  * [Slack](https://cloud-native.slack.com/archives/C06AH2C3K8B)
  * [Community Meetings](https://zoom-lfx.platform.linuxfoundation.org/meetings/kserve?view=month)
  * [Community Meetings Notes](https://docs.google.com/document/d/1KZUURwr9MnHXqHA08TFbfVbM8EAJSJjmaMhnvstvi-k)
  * [Get Involved](/website/docs/community/get-involved)
  * [Adopters](/website/docs/community/adopters)


More
  * [Blog](/website/blog)
  * [Presentations](/website/docs/community/presentations)
  * [GitHub](https://github.com/kserve/kserve)


Copyright © 2025 The KServe Authors. All rights reserved.   
The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [ Trademark Usage page. ](https://www.linuxfoundation.org/trademark-usage)
