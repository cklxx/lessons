# Versioning best practices (REST API) - Azure Storage | Microsoft Learn

- URL: https://learn.microsoft.com/en-us/rest/api/storageservices/versioning-best-practices
- Retrieved: 2025-12-18T10:13:37.080636+00:00

 Skip to main content  [ Skip to Ask Learn chat experience ]
This browser is no longer supported.
Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 
[ Download Microsoft Edge ](https://go.microsoft.com/fwlink/p/?LinkID=2092881 ) [ More info about Internet Explorer and Microsoft Edge ](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)
Table of contents  Exit editor mode
Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ] Add Add to plan [ Edit ](https://github.com/MicrosoftDocs/azure-docs-rest-apis/blob/main/docs-ref-conceptual/storageservices/Versioning-Best-Practices.md)
* * *
#### Share via
[ Facebook ] [ x.com ] [ LinkedIn ] [ Email ]
* * *
Print
* * *
Note
Access to this page requires authorization. You can try [signing in] or changing directories. 
Access to this page requires authorization. You can try changing directories. 
# Versioning best practices
Feedback
Summarize this article for me 
##  In this article 
Microsoft recommends the following versioning best practices for Azure Storage:
  * Explicitly specify the REST protocol version to use for every request.
  * Set a default version for Azure Blob Storage by using the [Set Blob Service Properties](https://learn.microsoft.com/en-us/rest/api/storageservices/set-blob-service-properties) operation. The default version specifies the version to use for anonymous requests for which the version header can't be set.
  * Client software that uses a shared access signature (SAS) URL to access storage resources might experience unexpected behavior when the SAS URL specifies a storage service version that's newer than the version that's used by the client software. To ensure that your clients work well with SAS tokens, we recommend the following approaches:
    * **For version 2014-02-14 and later** : If you're a SAS token consumer who's using the REST API, you can override the REST protocol version to specify the appropriate version by using the `api-version` parameter. For more information, see [Versioning for Azure Storage](https://learn.microsoft.com/en-us/rest/api/storageservices/versioning-for-the-azure-storage-services).
If you're a SAS token consumer who's using the Azure Storage client library, the library ensures that the correct REST protocol version is requested.
    * **For version 2013-08-15 and earlier** : Code that prepares and distributes shared access signature URLs (that is, SAS providers or generators) should specify versions that are understood by the client software (that is, SAS consumers) that's making storage service requests.
  * Always use the latest Azure Storage version to benefit from optimizations that are included with each new version. Some examples of such changes include:
    * Version 2013-08-15 introduced the JSON payload format that reduces network bandwidth usage by up to 70 percent compared to the OData AtomPub protocol.
    * Version 2013-08-15 allows SAS providers and generators to add certain response headers, such as `cache-control`, `content-disposition`, and `content-type` via SAS query parameters.
    * Version 2011-08-18 introduced the quoted `ETag` and `Accept-Ranges` response headers that are required for optimized download and streaming via browsers.


## See also
[Versioning for Azure Storage](https://learn.microsoft.com/en-us/rest/api/storageservices/versioning-for-the-azure-storage-services)
* * *
##  Additional resources 
* * *
  * Last updated on  2023-06-27 


### In this article
[en-us]
[ Your Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)
Theme
  * Light 
  * Dark 
  * High contrast 


  *   * [AI Disclaimer](https://learn.microsoft.com/en-us/principles-for-ai-generated-content)
  * [Previous Versions](https://learn.microsoft.com/en-us/previous-versions/)
  * [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
  * [Contribute](https://learn.microsoft.com/en-us/contribute)
  * [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
  * [Terms of Use](https://learn.microsoft.com/en-us/legal/termsofuse)
  * [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
  * (C) Microsoft 2025
