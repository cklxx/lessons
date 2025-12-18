# AIP-121: Resource-oriented design

- URL: https://cloud.google.com/apis/design/resources
- Retrieved: 2025-12-18T10:14:23.514501+00:00

[ AIPs ](https://cloud.google.com/ "Google")
 Jump to Content 
  * [Browse AIPs](https://cloud.google.com/general)
  * [News](https://cloud.google.com/news)
  * [FAQ](https://cloud.google.com/faq)
  * [Contributing](https://cloud.google.com/contributing)
  * [ API Linter  ](https://linter.aip.dev/)


Search this site
[ View on GitHub ](https://github.com/aip-dev/google.aip.dev)
[ AIPs ](https://cloud.google.com/ "Google")
 Jump to Content 
[ View on GitHub ](https://github.com/aip-dev/google.aip.dev)
  * AIPs by Scope
  * [General](https://cloud.google.com/general)
  * [Google Cloud Platform](https://cloud.google.com/cloud)
  * [Auth](https://cloud.google.com/auth)
  * [Client libraries](https://cloud.google.com/client-libraries)
  * [Workspace](https://cloud.google.com/apps)
  * [Actions on Google](https://cloud.google.com/aog)
  * AIPs
  * [ 1 AIP Purpose and Guidelines ](https://cloud.google.com/1)
  * [ 2 AIP Numbering ](https://cloud.google.com/2)
  * [ 3 AIP Versioning ](https://cloud.google.com/3)
  * [ 8 AIP Style and Guidance ](https://cloud.google.com/8)
  * [ 9 Glossary ](https://cloud.google.com/9)
  * [ 100 API Design Review FAQ ](https://cloud.google.com/100)
  * [ 111 Planes ](https://cloud.google.com/111)
  * [ 121 Resource-oriented design ](https://cloud.google.com/121)
  * [ 122 Resource names ](https://cloud.google.com/122)
  * [ 123 Resource types ](https://cloud.google.com/123)
  * [ 124 Resource association ](https://cloud.google.com/124)
  * [ 126 Enumerations ](https://cloud.google.com/126)
  * [ 127 HTTP and gRPC Transcoding ](https://cloud.google.com/127)
  * [ 128 Declarative-friendly interfaces ](https://cloud.google.com/128)
  * [ 129 Server-Modified Values and Defaults ](https://cloud.google.com/129)
  * [ 130 Methods ](https://cloud.google.com/130)
  * [ 131 Standard methods: Get ](https://cloud.google.com/131)
  * [ 132 Standard methods: List ](https://cloud.google.com/132)
  * [ 133 Standard methods: Create ](https://cloud.google.com/133)
  * [ 134 Standard methods: Update ](https://cloud.google.com/134)
  * [ 135 Standard methods: Delete ](https://cloud.google.com/135)
  * [ 136 Custom methods ](https://cloud.google.com/136)
  * [ 140 Field names ](https://cloud.google.com/140)
  * [ 141 Quantities ](https://cloud.google.com/141)
  * [ 142 Time and duration ](https://cloud.google.com/142)
  * [ 143 Standardized codes ](https://cloud.google.com/143)
  * [ 144 Repeated fields ](https://cloud.google.com/144)
  * [ 145 Ranges ](https://cloud.google.com/145)
  * [ 146 Generic fields ](https://cloud.google.com/146)
  * [ 147 Sensitive fields ](https://cloud.google.com/147)
  * [ 148 Standard fields ](https://cloud.google.com/148)
  * [ 149 Unset field values ](https://cloud.google.com/149)
  * [ 151 Long-running operations ](https://cloud.google.com/151)
  * [ 152 Jobs ](https://cloud.google.com/152)
  * [ 153 Import and export ](https://cloud.google.com/153)
  * [ 154 Resource freshness validation ](https://cloud.google.com/154)
  * [ 155 Request identification ](https://cloud.google.com/155)
  * [ 156 Singleton resources ](https://cloud.google.com/156)
  * [ 157 Partial responses ](https://cloud.google.com/157)
  * [ 158 Pagination ](https://cloud.google.com/158)
  * [ 159 Reading across collections ](https://cloud.google.com/159)
  * [ 160 Filtering ](https://cloud.google.com/160)
  * [ 161 Field masks ](https://cloud.google.com/161)
  * [ 162 Resource Revisions ](https://cloud.google.com/162)
  * [ 163 Change validation ](https://cloud.google.com/163)
  * [ 164 Soft delete ](https://cloud.google.com/164)
  * [ 165 Criteria-based delete ](https://cloud.google.com/165)
  * [ 180 Backwards compatibility ](https://cloud.google.com/180)
  * [ 181 Stability levels ](https://cloud.google.com/181)
  * [ 182 External software dependencies ](https://cloud.google.com/182)
  * [ 185 API Versioning ](https://cloud.google.com/185)
  * [ 190 Naming conventions ](https://cloud.google.com/190)
  * [ 191 File and directory structure ](https://cloud.google.com/191)
  * [ 192 Documentation ](https://cloud.google.com/192)
  * [ 193 Errors ](https://cloud.google.com/193)
  * [ 194 Automatic retry configuration ](https://cloud.google.com/194)
  * [ 200 Precedent ](https://cloud.google.com/200)
  * [ 202 Fields ](https://cloud.google.com/202)
  * [ 203 Field behavior documentation ](https://cloud.google.com/203)
  * [ 205 Beta-blocking changes ](https://cloud.google.com/205)
  * [ 210 Unicode ](https://cloud.google.com/210)
  * [ 211 Authorization checks ](https://cloud.google.com/211)
  * [ 213 Common components ](https://cloud.google.com/213)
  * [ 214 Resource expiration ](https://cloud.google.com/214)
  * [ 215 API-specific protos ](https://cloud.google.com/215)
  * [ 216 States ](https://cloud.google.com/216)
  * [ 217 Unreachable resources ](https://cloud.google.com/217)
  * [ 231 Batch methods: Get ](https://cloud.google.com/231)
  * [ 233 Batch methods: Create ](https://cloud.google.com/233)
  * [ 234 Batch methods: Update ](https://cloud.google.com/234)
  * [ 235 Batch methods: Delete ](https://cloud.google.com/235)
  * [ 236 Policy preview ](https://cloud.google.com/236)

Resource-oriented design  
---  
Number| 121  
Permalink| [google.aip.dev/121](https://google.aip.dev/121)  
State| Approved  
Created| 2019-01-26  
Updated| 2019-01-26  
Contents
  * Guidance
    * Resources
    * Methods
    * Strong Consistency
    * Stateless protocol
    * Cyclic References
  * Changelog


  * [File Bug](https://github.com/aip-dev/google.aip.dev/issues/)
  * [View source](https://github.com/aip-dev/google.aip.dev/blob/master/aip/general/0121.md)
  * [Edit this page](https://github.com/aip-dev/google.aip.dev/edit/master/aip/general/0121.md)


  1. [ API Improvement Proposals ](https://cloud.google.com/)
  2. [ General AIPs ](https://cloud.google.com/general)
  3. Resource-oriented design 


#### AIP-121
# Resource-oriented design
Resource-oriented design is a pattern for specifying [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) APIs, based on several high-level design principles (most of which are common to recent public HTTP APIs):
  * The fundamental building blocks of an API are individually-named _resources_ (nouns) and the relationships and hierarchy that exist between them.
  * A small number of standard _methods_ (verbs) provide the semantics for most common operations. However, custom methods are available in situations where the standard methods do not fit.
  * Stateless protocol: Each interaction between the client and the server is independent, and both the client and server have clear roles.


Readers might notice similarities between these principles and some principles of [REST](https://en.wikipedia.org/wiki/Representational_state_transfer); resource-oriented design borrows many principles from REST, while also defining its own patterns where appropriate.
## Guidance
When designing an API, consider the following (roughly in logical order):
  * The resources (nouns) the API will provide
  * The relationships and hierarchies between those resources
  * The schema of each resource
  * The methods (verbs) each resource provides, relying as much as possible on the standard verbs.


### Resources
A resource-oriented API **should** generally be modeled as a resource hierarchy, where each node is either a simple resource or a collection of resources.
A _collection_ contains resources of _the same type_. For example, a publisher has the collection of books that it publishes. A resource usually has fields, and resources may have any number of sub-resources (usually collections).
**Note:** While there is some conceptual alignment between storage systems and APIs, a service with a resource-oriented API is not necessarily a database, and has enormous flexibility in how it interprets resources and methods. API designers **should not** expect that their API will be reflective of their database schema. In fact, having an API that is identical to the underlying database schema is actually an anti-pattern, as it tightly couples the surface to the underlying system.
### Methods
Resource-oriented APIs emphasize resources (data model) over the methods performed on those resources (functionality). A typical resource-oriented API exposes a large number of resources with a small number of methods on each resource. The methods can be either the standard methods ([Get](https://cloud.google.com/131), [List](https://cloud.google.com/132), [Create](https://cloud.google.com/133), [Update](https://cloud.google.com/134), [Delete](https://cloud.google.com/135)), or [custom methods](https://cloud.google.com/136).
If the request to or the response from a standard method (or a custom method in the same _service_) **is** the resource or **contains** the resource, the resource schema for that resource across all methods **must** be the same.
Standard method | Request | Response  
---|---|---  
Create | Contains the resource | Is the resource  
Get | None | Is the resource  
Update | Contains the resource | Is the resource  
Delete | None | None  
List | None | Contains the resources  
_The table above describes each standard method's relationship to the resource, where "None" indicates that the resource neither_ _is_ _nor_ _is contained_ _in the request or the response_
A resource **must** support at minimum [Get](https://cloud.google.com/131): clients must be able to validate the state of resources after performing a mutation such as [Create](https://cloud.google.com/133), [Update](https://cloud.google.com/134), or [Delete](https://cloud.google.com/135).
A resource **must** also support [List](https://cloud.google.com/132), except for [singleton resources](https://cloud.google.com/156) where more than one resource is not possible.
**Note:** A custom method in resource-oriented design does _not_ entail defining a new or custom HTTP verb. Custom methods use traditional HTTP verbs (usually `POST`) and define the custom verb in the URI.
APIs **should** prefer standard methods over custom methods; the purpose of custom methods is to define functionality that does not cleanly map to any of the standard methods. Custom methods offer the same design freedom as traditional RPC APIs, which can be used to implement common programming patterns, such as database transactions, import and export, or data analysis.
### Strong Consistency
For methods that operate on the [management plane](https://cloud.google.com/111#management-plane), the completion of those operations (either successful or with an error, long-running operation, or synchronous) **must** mean that the state of the resource's existence and all user-settable values have reached a steady-state.
[Output only](https://cloud.google.com/203#output-only) values unrelated to the resource [state](https://cloud.google.com/216) **should** also have reached a steady-state for values that are related to the resource [state](https://cloud.google.com/216).
Examples include:
  * Following a successful create that is the latest mutation on a resource, a get request for a resource **must** return the resource.
  * Following a successful update that is the latest mutation on a resource, a get request for a resource **must** return the final values from the update request.
  * Following a successful delete that is the latest mutation on a resource, a get request for a resource **must** return `NOT_FOUND` (or the resource with the `DELETED` state value in the case of [soft delete](https://cloud.google.com/164))


Clients of resource-oriented APIs often need to orchestrate multiple operations in sequence (e.g. create resource A, create resource B which depends on A), and ensuring that resources immediately reflect steady user state after an operation is complete ensures clients can rely on method completion as a signal to begin the next operation.
[Output only](https://cloud.google.com/203#output-only) fields ideally would follow the same guidelines, but as these fields can often represent a resource's live state, it's sometimes necessary for these values to change after a successful mutation operation to reflect a state change.
### Stateless protocol
As with most public APIs available today, resource-oriented APIs **must** operate over a [stateless protocol](https://en.wikipedia.org/wiki/Stateless_protocol): The fundamental behavior of any individual request is independent of other requests made by the caller. This is to say, each request happens in isolation of other requests made by that client or another, and resources exposed by an API are directly addressable without needing to apply a series of specific requests to "reach" the desired resource.
In an API with a stateless protocol, the server has the responsibility for persisting data, which may be shared between multiple clients, while clients have sole responsibility and authority for maintaining the application state.
### Cyclic References
The relationship between resources, such as with [resource references](https://cloud.google.com/122#fields-representing-another-resource), **must** be representable via a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph). The parent-child relationship also **must** be acyclic, and as per [AIP-124](https://cloud.google.com/124) a given resource instance will only have one canonical parent resource.
A cyclic relationship between resources increases the complexity of managing resources. Consider resources A and B that refer to each other. The process to create said resources are:
  1. create resource A without a reference to B. Retrieve id for resource A.
  2. create resource B with a reference to A. Retrieve id for resource B.
  3. update resource A with the reference to B.


The delete operation may also become more complex, due to reasoning about which resource must be dereferenced first for a successful deletion.
This requirement does not apply to relationships that are expressed via [output only](https://cloud.google.com/203#output-only) fields, as they do not require the user to specify the values and in turn do not increase resource management complexity.
## Changelog
  * **2024-07-08** : Clarify acyclic nature of parent-child relationship.
  * **2023-08-24** : Added guidance on consistency guarantees of methods.
  * **2023-07-23** : Clarify stateless protocol definition.
  * **2023-01-21** : Explicitly require matching schema across standard methods.
  * **2022-12-19** : Added a section requiring Get and List.
  * **2022-11-02** : Added a section restricting resource references.
  * **2019-08-01** : Changed the examples from "shelves" to "publishers", to present a better example of resource ownership.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see [content licensing](https://cloud.google.com/licensing).
