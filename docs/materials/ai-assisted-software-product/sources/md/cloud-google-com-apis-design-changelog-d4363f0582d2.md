# Changelog &nbsp;|&nbsp; Cloud API Design Guide &nbsp;|&nbsp; Google Cloud Documentation

- URL: https://cloud.google.com/apis/design/changelog
- Retrieved: 2025-12-18T10:14:32.612809+00:00

 Skip to main content 
(https://cloud.google.com/)
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
(https://cloud.google.com/)
  * 

  * [ Technology areas  ](https://cloud.google.com/docs)
    * More 
  * [ Cross-product tools  ](https://cloud.google.com/docs/cross-product-overviews)
    * More 
  * [ Console  ](https://console.cloud.google.com/)


  * Discover
  * [Google Cloud APIs](https://cloud.google.com/apis/docs/overview)
  * [Google Enterprise APIs](https://cloud.google.com/apis/docs/resources/enterprise-apis)
  * Get started
  * [Getting started](https://cloud.google.com/apis/docs/getting-started)
  * [Capping API usage](https://cloud.google.com/apis/docs/capping-api-usage)
  * [Monitoring API usage](https://cloud.google.com/apis/docs/monitoring)
  * [Troubleshooting API usage](https://cloud.google.com/apis/docs/troubleshooting)
  * [HTTP guidelines](https://cloud.google.com/apis/docs/http)
  * [System parameters](https://cloud.google.com/apis/docs/system-parameters)
  * API design guide
  * [Introduction](https://cloud.google.com/apis/design)
  * [Directory structure](https://cloud.google.com/apis/design/directory_structure)
  * [Changelog](https://cloud.google.com/apis/design/changelog)


  * [ AI and ML  ](https://cloud.google.com/docs/ai-ml)
  * [ Application development  ](https://cloud.google.com/docs/application-development)
  * [ Application hosting  ](https://cloud.google.com/docs/application-hosting)
  * [ Compute  ](https://cloud.google.com/docs/compute-area)
  * [ Data analytics and pipelines  ](https://cloud.google.com/docs/data)
  * [ Databases  ](https://cloud.google.com/docs/databases)
  * [ Distributed, hybrid, and multicloud  ](https://cloud.google.com/docs/dhm-cloud)
  * [ Generative AI  ](https://cloud.google.com/docs/generative-ai)
  * [ Industry solutions  ](https://cloud.google.com/docs/industry)
  * [ Networking  ](https://cloud.google.com/docs/networking)
  * [ Observability and monitoring  ](https://cloud.google.com/docs/observability)
  * [ Security  ](https://cloud.google.com/docs/security)
  * [ Storage  ](https://cloud.google.com/docs/storage)


  * [ Access and resources management  ](https://cloud.google.com/docs/access-resources)
  * [ Costs and usage management  ](https://cloud.google.com/docs/costs-usage)
  * [ Infrastructure as code  ](https://cloud.google.com/docs/iac)
  * [ Migration  ](https://cloud.google.com/docs/migration)
  * [ SDK, languages, frameworks, and tools  ](https://cloud.google.com/docs/devtools)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Cloud API Design Guide ](https://docs.cloud.google.com/apis/design)


Send feedback 
#  Changelog Stay organized with collections  Save and categorize content based on your preferences. 
This Changelog highlights notable changes to the [API Design Guide](https://cloud.google.com/apis/design).
## 2025-06
  * Redirected Design page Naming Convention to Google AIP.


## 2024-10
  * Redirected Design pages to Google AIPs, except for Directory Structure and Naming Conventions.


## 2021-12
  * Changed terminology Networked API to Network API for consistency with https://google.aip.dev/9.


## 2021-09
  * Document both Google API error format v1 and v2.


## 2021-04
  * Introduced visibility-based versioning.
  * Introduced API title to glossary.


## 2021-03
  * Added annotation for output only fields.
  * Update enum value guidance to always include an explicit `_UNSPECIFIED` value.
  * Add guidance on how to generate and parse resource names.
  * Add `progress_percent` to standard fields.


## 2021-02
  * Added guidance on proto3 `optional` primitive fields.


## 2021-01
  * Updated the Errors page to cover the latest improvement related to `google.rpc.ErrorInfo` and `google.api.ErrorReason`.
  * Added guidance on how to use `oauth2l`, `curl`, and System Parameters to troubleshoot errors with Google APIs.
  * Added `502` error code explanation to the Errors page. It is a network error instead of an API error.


## 2020-12
  * Package names should use singlar component names for global consistency. Package names must not use underscores.


## 2020-09
  * Cleaned up some field description requirements; changed some uses of "must" outside RFC 2119 to be RFC 2119 "should" directives.
  * Removed the `bool deleted` standard field, in favor of `google.protobuf.Timestamp delete_time` (which was already listed).


## 2020-07
  * Updated documentation.md to match https://google.aip.dev/192#formatting. Markdown tables and raw HTML must not be used in proto comments.
  * Added `ErrorInfo` for error handling.
  * Added Large Payloads for design patterns.


## 2020-04
  * Renamed Cloud APIs to Google Cloud APIs in glossary.
  * Introduced API and service as synonyms of API service.


## 2020-02
  * Updated versioning to add two versioning strategies (channel-based and release-based), remove guidance on point versions, and change how we refer to semantic versioning.


## 2020-01
  * Add data retention to design patterns.


## 2019-11
  * Add terminology Cloud APIs to glossary.
  * Recommend clients to retry only for UNAVAILABLE errors.


## 2019-06
  * Add "Bool vs Enum vs String" to design patterns.


## 2019-03
  * Add system parameters to standard fields.


## 2019-02
  * Add domain-scoped names to design patterns.


## 2018-03
  * Add streaming half-close semantics to design patterns.


## 2018-02
  * Add `read_time` to Standard Fields.


## 2018-01
  * Add schema reference for API Service Definition.


## 2017-12
  * Clarify API major version must be the last component of proto package name.


## 2017-11
  * Clarify why the `Create` method take an input resource.
  * Clarify collection IDs that don't have plural form, such as evidence and weather.
  * Add singleton resource to design patterns.
  * Clarify C# naming conventions for acronyms and versions.


## 2017-09
  * Add `mime_type` to standard fields.
  * Add `expire_time` to standard fields.
  * Add `start_time` and `end_time` to standard fields.


## 2017-02
  * Add "API endpoint" to glossary.
  * Add `update_mask` to standard fields.
  * Add a link to `FieldMask` to standard methods.
  * Mention that OpenAPI spec does not support unsigned integers.
  * Clarify that method names should use verbs in the imperative mood.


[ Previous arrow_back  Directory structure  ](https://cloud.google.com/apis/design/directory_structure)
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
    * [ Getting Started with Google Cloud ](https://cloud.google.com/docs/get-started/)
    * [ Code samples ](https://cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://cloud.google.com/architecture/)
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
