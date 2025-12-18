# API design guide &nbsp;|&nbsp; Cloud API Design Guide &nbsp;|&nbsp; Google Cloud Documentation

- URL: https://docs.cloud.google.com/apis/design
- Retrieved: 2025-12-18T10:14:24.353543+00:00

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
#  API design guide Stay organized with collections  Save and categorize content based on your preferences. 
[Changelog](https://cloud.google.com/apis/design/changelog)
## Introduction
This is a general design guide for networked APIs. It has been used inside Google since 2014 and is the guide that Google follows when designing [Cloud APIs](https://docs.cloud.google.com/apis/docs/overview) and other [Google APIs](https://github.com/googleapis/googleapis). This design guide is shared here to inform outside developers and to make it easier for us all to work together.
[Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc) developers may find this guide particularly useful when designing gRPC APIs, and we strongly recommend such developers use these design principles. However, we don't mandate its use. You can use Cloud Endpoints and gRPC without following the guide.
This guide applies to both REST APIs and RPC APIs, with specific focus on gRPC APIs. gRPC APIs use [Protocol Buffers](https://docs.cloud.google.com/apis/design/proto3) to define their API surface and [API Service Configuration](https://github.com/googleapis/googleapis/blob/master/google/api/service.proto) to configure their API services, including HTTP mapping, logging, and monitoring. HTTP mapping features are used by Google APIs and Cloud Endpoints gRPC APIs for JSON/HTTP to Protocol Buffers/RPC [transcoding](https://docs.cloud.google.com/endpoints/docs/transcoding).
This guide is a living document and additions to it will be made over time as new style and design patterns are adopted and approved. In that spirit, it is never going to be complete and there will always be ample room for the art and craft of API design.
## Conventions Used in This Guide
The requirement level keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" used in this document are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).
In this document, such keywords are highlighted using **bold** font.
## Sections
### Resource-oriented Design
For information about implementing resource-oriented design for RPC and REST APIs, see [AIP-121](https://google.aip.dev/121).
### Resource Names
For information about resource names, see [AIP-122](https://google.aip.dev/122).
### Standard Methods
For general information about methods, see [AIP-130](https://google.aip.dev/130).
For information about standard methods, see the following AIPs:
  * For `Get`, see [AIP-131](https://google.aip.dev/131)
  * For `List`, see [AIP-132](https://google.aip.dev/132)
  * For `Create`, see [AIP-133](https://google.aip.dev/133)
  * For `Update`, see [AIP-134](https://google.aip.dev/134)
  * For `Delete`, see [AIP-135](https://google.aip.dev/135)


### Custom Methods
For information about custom methods, see [AIP-136](https://google.aip.dev/136).
### Additional topics
For information about the following topics, see their related AIPs.
  * For **Standard fields** , see [AIP-148](https://google.aip.dev/148)
  * For **Errors** , see [AIP-193](https://google.aip.dev/193)
  * For **Design patterns** , see [AIP guidance on design patterns](https://google.aip.dev/general#design-patterns)
  * For **Inline API documentation** , see [AIP-192](https://google.aip.dev/192)
  * For **Using proto3** , see [the Syntax section of AIP-191](https://google.aip.dev/191#syntax)
  * For **Versioning** , see [AIP-185](https://google.aip.dev/185)
  * For **Backward compatibility** , see [AIP-180](https://google.aip.dev/180)
  * For **File structure** , see [the File Layout section of AIP-191](https://google.aip.dev/191#file-layout)
  * For a **Glossary** of terms, see [AIP-9](https://google.aip.dev/9)
  * For **Naming conventions** , see [AIP-190](https://google.aip.dev/190)


For information about the following topics, see their related pages in this guide.
  * [Directory Structure](https://cloud.google.com/apis/design/directory_structure)


[ Next Directory structure  arrow_forward  ](https://docs.cloud.google.com/apis/design/directory_structure)
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
