# Directory structure &nbsp;|&nbsp; Cloud API Design Guide &nbsp;|&nbsp; Google Cloud Documentation

- URL: https://docs.cloud.google.com/apis/design/directory_structure
- Retrieved: 2025-12-18T10:14:33.626007+00:00

 Skip to main content 
(https://docs.cloud.google.com/)
  * 

[ Technology areas ](https://docs.cloud.google.com/docs)
  * [ AI and ML  ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Application development  ](https://docs.cloud.google.com/docs/application-development)
  * [ Application hosting  ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Compute  ](https://docs.cloud.google.com/docs/compute-area)
  * [ Data analytics and pipelines  ](https://docs.cloud.google.com/docs/data)
  * [ Databases  ](https://docs.cloud.google.com/docs/databases)
  * [ Distributed, hybrid, and multicloud  ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Generative AI  ](https://docs.cloud.google.com/docs/generative-ai)
  * [ Industry solutions  ](https://docs.cloud.google.com/docs/industry)
  * [ Networking  ](https://docs.cloud.google.com/docs/networking)
  * [ Observability and monitoring  ](https://docs.cloud.google.com/docs/observability)
  * [ Security  ](https://docs.cloud.google.com/docs/security)
  * [ Storage  ](https://docs.cloud.google.com/docs/storage)


[ Cross-product tools ](https://docs.cloud.google.com/docs/cross-product-overviews)
  * [ Access and resources management  ](https://docs.cloud.google.com/docs/access-resources)
  * [ Costs and usage management  ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Infrastructure as code  ](https://docs.cloud.google.com/docs/iac)
  * [ Migration  ](https://docs.cloud.google.com/docs/migration)
  * [ SDK, languages, frameworks, and tools  ](https://docs.cloud.google.com/docs/devtools)


`/`
[ Console ](https://console.cloud.google.com/)
  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어

Sign in
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Cloud API Design Guide ](https://docs.cloud.google.com/apis/design)


[Start free](https://console.cloud.google.com/freetrial)
(https://docs.cloud.google.com/)
  * 

  * [ Technology areas  ](https://docs.cloud.google.com/docs)
    * More 
  * [ Cross-product tools  ](https://docs.cloud.google.com/docs/cross-product-overviews)
    * More 
  * [ Console  ](https://console.cloud.google.com/)


  * Discover
  * [Google Cloud APIs](https://docs.cloud.google.com/apis/docs/overview)
  * [Google Enterprise APIs](https://docs.cloud.google.com/apis/docs/resources/enterprise-apis)
  * Get started
  * [Getting started](https://docs.cloud.google.com/apis/docs/getting-started)
  * [Capping API usage](https://docs.cloud.google.com/apis/docs/capping-api-usage)
  * [Monitoring API usage](https://docs.cloud.google.com/apis/docs/monitoring)
  * [Troubleshooting API usage](https://docs.cloud.google.com/apis/docs/troubleshooting)
  * [HTTP guidelines](https://docs.cloud.google.com/apis/docs/http)
  * [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters)
  * API design guide
  * [Introduction](https://docs.cloud.google.com/apis/design)
  * [Directory structure](https://docs.cloud.google.com/apis/design/directory_structure)
  * [Changelog](https://docs.cloud.google.com/apis/design/changelog)


  * [ AI and ML  ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Application development  ](https://docs.cloud.google.com/docs/application-development)
  * [ Application hosting  ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Compute  ](https://docs.cloud.google.com/docs/compute-area)
  * [ Data analytics and pipelines  ](https://docs.cloud.google.com/docs/data)
  * [ Databases  ](https://docs.cloud.google.com/docs/databases)
  * [ Distributed, hybrid, and multicloud  ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Generative AI  ](https://docs.cloud.google.com/docs/generative-ai)
  * [ Industry solutions  ](https://docs.cloud.google.com/docs/industry)
  * [ Networking  ](https://docs.cloud.google.com/docs/networking)
  * [ Observability and monitoring  ](https://docs.cloud.google.com/docs/observability)
  * [ Security  ](https://docs.cloud.google.com/docs/security)
  * [ Storage  ](https://docs.cloud.google.com/docs/storage)


  * [ Access and resources management  ](https://docs.cloud.google.com/docs/access-resources)
  * [ Costs and usage management  ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Infrastructure as code  ](https://docs.cloud.google.com/docs/iac)
  * [ Migration  ](https://docs.cloud.google.com/docs/migration)
  * [ SDK, languages, frameworks, and tools  ](https://docs.cloud.google.com/docs/devtools)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Cloud API Design Guide ](https://docs.cloud.google.com/apis/design)


Send feedback 
#  Directory structure Stay organized with collections  Save and categorize content based on your preferences. 
API services typically use `.proto` files to define the API surface and `.yaml` files to configure the API service. Each API service **must** have an API directory inside an API repository. The API directory **should** contain all API definition files and build scripts.
Each API directory **should** have the following standard layout:
  * API directory
    * Repository prerequisites
      * `BUILD` \- The build file.
      * `METADATA` \- The build metadata file.
      * `OWNERS` \- The API directory owners.
      * `README.md` \- The general information about the API service.
    * Configuration files
      * `{service}.yaml` \- The baseline service config file, which is the YAML representation of the `google.api.Service` proto message.
      * `prod.yaml` \- The prod delta service config file.
      * `staging.yaml` \- The staging delta service config file.
      * `test.yaml` \- The test delta service config file.
      * `local.yaml` \- The local delta service config file.
    * Documentation files
      * `doc/*` \- The technical documentation files. They should be in Markdown format.
    * Interface definitions
      * `v[0-9]*/*` \- Each such directory contains a major version of the API, mainly the proto files and build scripts.
      * `{subapi}/v[0-9]*/*` \- Each `{subapi}` directory contains interface definition of a sub-API. Each sub-API may have its own independent major version.
      * `type/*` \- proto files containing types that are shared between different APIs, different versions of the same API, or between the API and service implementation. Type definitions under `type/*` **should** not have breaking changes once they are released.


Public Google API definitions are published on GitHub, see [Google APIs](https://github.com/googleapis/googleapis) repository.
**Note:** If you are a [Cloud Endpoints](https://docs.cloud.google.com/endpoints) developer, you can follow [Configuring a gRPC service](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) to configure your API service.
[ Previous arrow_back  Introduction  ](https://docs.cloud.google.com/apis/design)
[ Next Changelog  arrow_forward  ](https://docs.cloud.google.com/apis/design/changelog)
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-12-15 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-15 UTC."],,] 
  * ### Products and pricing
    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support
    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources
    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage
    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)


  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * [ Manage cookies ]
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)


  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어
