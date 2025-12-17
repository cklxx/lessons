# [2309.06180] Efficient Memory Management for Large Language Model Serving with PagedAttention

- URL: https://arxiv.org/abs/2309.06180
- PDF: https://arxiv.org/pdf/2309.06180.pdf
- Retrieved: 2025-12-17T17:00:36.779745+00:00

## Abstract page (HTML → Markdown)

[Skip to main content](#content)
[](https://www.cornell.edu/)
In just 5 minutes help us improve arXiv:
[Annual Global Survey](https://cornell.ca1.qualtrics.com/jfe/form/SV_6kZEJCkEgp3yGZo)
We gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors. [Donate](https://info.arxiv.org/about/donate.html)
[](/IgnoreMe)
[](/) > [cs](/list/cs/recent) > arXiv:2309.06180 
[Help](https://info.arxiv.org/help) | [Advanced Search](https://arxiv.org/search/advanced)
All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text
Search
[](https://arxiv.org/)
[ ](https://www.cornell.edu/)
open search
GO
open navigation menu
## quick links
  * [Login](https://arxiv.org/login)
  * [Help Pages](https://info.arxiv.org/help)
  * [About](https://info.arxiv.org/about)


# Computer Science > Machine Learning
**arXiv:2309.06180** (cs) 
[Submitted on 12 Sep 2023]
# Title:Efficient Memory Management for Large Language Model Serving with PagedAttention
Authors:[Woosuk Kwon](https://arxiv.org/search/cs?searchtype=author&query=Kwon,+W), [Zhuohan Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z), [Siyuan Zhuang](https://arxiv.org/search/cs?searchtype=author&query=Zhuang,+S), [Ying Sheng](https://arxiv.org/search/cs?searchtype=author&query=Sheng,+Y), [Lianmin Zheng](https://arxiv.org/search/cs?searchtype=author&query=Zheng,+L), [Cody Hao Yu](https://arxiv.org/search/cs?searchtype=author&query=Yu,+C+H), [Joseph E. Gonzalez](https://arxiv.org/search/cs?searchtype=author&query=Gonzalez,+J+E), [Hao Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+H), [Ion Stoica](https://arxiv.org/search/cs?searchtype=author&query=Stoica,+I)
View a PDF of the paper titled Efficient Memory Management for Large Language Model Serving with PagedAttention, by Woosuk Kwon and 8 other authors
[View PDF](/pdf/2309.06180)
> Abstract:High throughput serving of large language models (LLMs) requires batching sufficiently many requests at a time. However, existing systems struggle because the key-value cache (KV cache) memory for each request is huge and grows and shrinks dynamically. When managed inefficiently, this memory can be significantly wasted by fragmentation and redundant duplication, limiting the batch size. To address this problem, we propose PagedAttention, an attention algorithm inspired by the classical virtual memory and paging techniques in operating systems. On top of it, we build vLLM, an LLM serving system that achieves (1) near-zero waste in KV cache memory and (2) flexible sharing of KV cache within and across requests to further reduce memory usage. Our evaluations show that vLLM improves the throughput of popular LLMs by 2-4$\times$ with the same level of latency compared to the state-of-the-art systems, such as FasterTransformer and Orca. The improvement is more pronounced with longer sequences, larger models, and more complex decoding algorithms. vLLM's source code is publicly available at [this https URL](https://github.com/vllm-project/vllm)
Comments: | SOSP 2023  
---|---  
Subjects: |  Machine Learning (cs.LG); Distributed, Parallel, and Cluster Computing (cs.DC)  
Cite as: | [arXiv:2309.06180](https://arxiv.org/abs/2309.06180) [cs.LG]  
  | (or  [arXiv:2309.06180v1](https://arxiv.org/abs/2309.06180v1) [cs.LG] for this version)   
  |  <https://doi.org/10.48550/arXiv.2309.06180> Focus to learn more arXiv-issued DOI via DataCite  
## Submission history
From: Woosuk Kwon [[view email](/show-email/2fbc22fc/2309.06180)]   
**[v1]** Tue, 12 Sep 2023 12:50:04 UTC (831 KB)  

Full-text links:
## Access Paper:
View a PDF of the paper titled Efficient Memory Management for Large Language Model Serving with PagedAttention, by Woosuk Kwon and 8 other authors
  * [View PDF](/pdf/2309.06180)
  * [TeX Source ](/src/2309.06180)


[ view license ](http://creativecommons.org/licenses/by/4.0/ "Rights to this article")
Current browse context: 
cs.LG
[< prev](/prevnext?id=2309.06180&function=prev&context=cs.LG "previous in cs.LG \(accesskey p\)")   |   [next >](/prevnext?id=2309.06180&function=next&context=cs.LG "next in cs.LG \(accesskey n\)")   

[new](/list/cs.LG/new) |  [recent](/list/cs.LG/recent) | [2023-09](/list/cs.LG/2023-09)
Change to browse by: 
[cs](/abs/2309.06180?context=cs)  
[cs.DC](/abs/2309.06180?context=cs.DC)  

### References & Citations
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2309.06180)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2309.06180)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2309.06180)


### [ 1 blog link](/tb/2309.06180)
([what is this?](https://info.arxiv.org/help/trackback.html)) 
export BibTeX citation Loading...
## BibTeX formatted citation
×
loading...
Data provided by: 
### Bookmark
[ ](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2309.06180&description=Efficient Memory Management for Large Language Model Serving with PagedAttention "Bookmark on BibSonomy") [ ](https://reddit.com/submit?url=https://arxiv.org/abs/2309.06180&title=Efficient Memory Management for Large Language Model Serving with PagedAttention "Bookmark on Reddit")
Bibliographic Tools
# Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer _([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))_
Connected Papers Toggle
Connected Papers _([What is Connected Papers?](https://www.connectedpapers.com/about))_
Litmaps Toggle
Litmaps _([What is Litmaps?](https://www.litmaps.co/))_
scite.ai Toggle
scite Smart Citations _([What are Smart Citations?](https://www.scite.ai/))_
Code, Data, Media
# Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv _([What is alphaXiv?](https://alphaxiv.org/))_
Links to Code Toggle
CatalyzeX Code Finder for Papers _([What is CatalyzeX?](https://www.catalyzex.com))_
DagsHub Toggle
DagsHub _([What is DagsHub?](https://dagshub.com/))_
GotitPub Toggle
Gotit.pub _([What is GotitPub?](http://gotit.pub/faq))_
Huggingface Toggle
Hugging Face _([What is Huggingface?](https://huggingface.co/huggingface))_
Links to Code Toggle
Papers with Code _([What is Papers with Code?](https://paperswithcode.com/))_
ScienceCast Toggle
ScienceCast _([What is ScienceCast?](https://sciencecast.org/welcome))_
Demos
# Demos
Replicate Toggle
Replicate _([What is Replicate?](https://replicate.com/docs/arxiv/about))_
Spaces Toggle
Hugging Face Spaces _([What is Spaces?](https://huggingface.co/docs/hub/spaces))_
Spaces Toggle
TXYZ.AI _([What is TXYZ.AI?](https://txyz.ai))_
Related Papers
# Recommenders and Search Tools
Link to Influence Flower
Influence Flower _([What are Influence Flowers?](https://influencemap.cmlab.dev/))_
Core recommender toggle
CORE Recommender _([What is CORE?](https://core.ac.uk/services/recommender))_
IArxiv recommender toggle
IArxiv Recommender _([What is IArxiv?](https://iarxiv.org/about))_
  * Author
  * Venue
  * Institution
  * Topic


About arXivLabs 
# arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).
[Which authors of this paper are endorsers?](/auth/show-endorsers/2309.06180) | [Disable MathJax](javascript:setMathjaxCookie\(\)) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html)) 
  * [About](https://info.arxiv.org/about)
  * [Help](https://info.arxiv.org/help)


  * contact arXivClick here to contact arXiv [ Contact](https://info.arxiv.org/help/contact.html)
  * subscribe to arXiv mailingsClick here to subscribe [ Subscribe](https://info.arxiv.org/help/subscribe)


  * [Copyright](https://info.arxiv.org/help/license/index.html)
  * [Privacy Policy](https://info.arxiv.org/help/policies/privacy_policy.html)


  * [Web Accessibility Assistance](https://info.arxiv.org/help/web_accessibility.html)
  * [arXiv Operational Status ](https://status.arxiv.org)

## Full text (PDF → text)

```text
                                             Efficient Memory Management for Large Language
                                                     Model Serving with PagedAttention
                                              Woosuk Kwon1,∗ Zhuohan Li1,∗ Siyuan Zhuang1 Ying Sheng1,2 Lianmin Zheng1 Cody Hao Yu3
                                                                   Joseph E. Gonzalez1 Hao Zhang4 Ion Stoica1
                                                                      1 UC Berkeley       2 Stanford University            3 Independent Researcher          4 UC San Diego


                                         Abstract                                                                                                                                                           Existing systems            vLLM
                                                                                                                                                                                                  40




                                                                                                                                                                              Memory usage (GB)
                                         High throughput serving of large language models (LLMs)
                                         requires batching sufficiently many requests at a time. How-
arXiv:2309.06180v1 [cs.LG] 12 Sep 2023




                                                                                                                                                                                                  30

                                         ever, existing systems struggle because the key-value cache                                                      KV
                                                                                                                                     Parameters          Cache                                             Parameter size
                                         (KV cache) memory for each request is huge and grows                                                           (>30%)                                    20
                                                                                                                                    (26GB, 65%)




                                                                                                                                                                  Throughput (token/s)
                                         and shrinks dynamically. When managed inefficiently, this                                                                                       1.2k


                                         memory can be significantly wasted by fragmentation and                                                                                         0.8k
                                                                                                                                                        Others
                                         redundant duplication, limiting the batch size. To address                                                                                      0.4k
                                         this problem, we propose PagedAttention, an attention al-                                    NVIDIA A100 40GB
                                                                                                                                                                                                  0
                                         gorithm inspired by the classical virtual memory and pag-                                                                                                     0       10           20   30       40
                                                                                                                                                                                                              Batch size (# requests)
                                         ing techniques in operating systems. On top of it, we build
                                         vLLM, an LLM serving system that achieves (1) near-zero                                Figure 1. Left: Memory layout when serving an LLM with
                                         waste in KV cache memory and (2) flexible sharing of KV                                13B parameters on NVIDIA A100. The parameters (gray)
                                         cache within and across requests to further reduce mem-                                persist in GPU memory throughout serving. The memory
                                         ory usage. Our evaluations show that vLLM improves the                                 for the KV cache (red) is (de)allocated per serving request.
                                         throughput of popular LLMs by 2-4× with the same level                                 A small amount of memory (yellow) is used ephemerally
                                         of latency compared to the state-of-the-art systems, such                              for activation. Right: vLLM smooths out the rapid growth
                                         as FasterTransformer and Orca. The improvement is more                                 curve of KV cache memory seen in existing systems [31, 60],
                                         pronounced with longer sequences, larger models, and more                              leading to a notable boost in serving throughput.
                                         complex decoding algorithms. vLLM’s source code is publicly
                                         available at https://github.com/vllm-project/vllm.                                     the cost per request—of LLM serving systems is becoming
                                                                                                                                more important.
                                         1    Introduction                                                                          At the core of LLMs lies an autoregressive Transformer
                                                                                                                                model [53]. This model generates words (tokens), one at a
                                         The emergence of large language models (LLMs) like GPT [5,
                                                                                                                                time, based on the input (prompt) and the previous sequence
                                         37] and PaLM [9] have enabled new applications such as pro-
                                                                                                                                of the output’s tokens it has generated so far. For each re-
                                         gramming assistants [6, 18] and universal chatbots [19, 35]
                                                                                                                                quest, this expensive process is repeated until the model out-
                                         that are starting to profoundly impact our work and daily
                                                                                                                                puts a termination token. This sequential generation process
                                         routines. Many cloud companies [34, 44] are racing to pro-
                                                                                                                                makes the workload memory-bound, underutilizing the com-
                                         vide these applications as hosted services. However, running
                                                                                                                                putation power of GPUs and limiting the serving throughput.
                                         these applications is very expensive, requiring a large num-
                                                                                                                                   Improving the throughput is possible by batching multi-
                                         ber of hardware accelerators such as GPUs. According to
                                                                                                                                ple requests together. However, to process many requests
                                         recent estimates, processing an LLM request can be 10× more
                                                                                                                                in a batch, the memory space for each request should be
                                         expensive than a traditional keyword query [43]. Given these
                                                                                                                                efficiently managed. For example, Fig. 1 (left) illustrates the
                                         high costs, increasing the throughput—and hence reducing
                                                                                                                                memory distribution for a 13B-parameter LLM on an NVIDIA
                                                                                                                                A100 GPU with 40GB RAM. Approximately 65% of the mem-
                                         Permission to make digital or hard copies of part or all of this work for              ory is allocated for the model weights, which remain static
                                         personal or classroom use is granted without fee provided that copies are
                                                                                                                                during serving. Close to 30% of the memory is used to store
                                         not made or distributed for profit or commercial advantage and that copies
                                         bear this notice and the full citation on the first page. Copyrights for third-        the dynamic states of the requests. For Transformers, these
                                         party components of this work must be honored. For all other uses, contact             states consist of the key and value tensors associated with the
                                         the owner/author(s).                                                                   attention mechanism, commonly referred to as KV cache [41],
                                         SOSP ’23, October 23–26, 2023, Koblenz, Germany                                        which represent the context from earlier tokens to gener-
                                         © 2023 Copyright held by the owner/author(s).                                          ate new output tokens in sequence. The remaining small
                                         ACM ISBN 979-8-4007-0229-7/23/10.
                                         https://doi.org/10.1145/3600006.3613165                                                ∗ Equal contribution.

                                                                                                                            1
                                                                                               decoding algorithms, such as parallel sampling and beam
                                                                          External frag.
                            Token states   Reservation   Internal frag.   & Others             search, that generate multiple outputs per request. In these
                      100
                               8.9                                                             scenarios, the request consists of multiple sequences that can
                      80                     41.6           36.6                               partially share their KV cache. However, memory sharing is
 KV cache usage (%)




                                                                                               not possible in the existing systems because the KV cache of
                      60
                              57.3
                                             13.6           25.2
                                                                                               the sequences is stored in separate contiguous spaces.
                                                                            96.3
                      40                                                                          To address the above limitations, we propose PagedAt-
                                             17.9
                              13.3                                                             tention, an attention algorithm inspired by the operating
                      20                                    38.2
                              20.4
                                             26.8                                              system’s (OS) solution to memory fragmentation and shar-
                       0                                                                       ing: virtual memory with paging. PagedAttention divides the
                               Orca          Orca           Orca            vLLM
                              (Max)         (Pow2)        (Oracle)                             request’s KV cache into blocks, each of which can contain
                                                                                               the attention keys and values of a fixed number of tokens. In
Figure 2. Average percentage of memory wastes in different                                     PagedAttention, the blocks for the KV cache are not neces-
LLM serving systems during the experiment in §6.2.                                             sarily stored in contiguous space. Therefore, we can manage
                                                                                               the KV cache in a more flexible way as in OS’s virtual mem-
                                                                                               ory: one can think of blocks as pages, tokens as bytes, and
percentage of memory is used for other data, including ac-                                     requests as processes. This design alleviates internal frag-
tivations – the ephemeral tensors created when evaluating                                      mentation by using relatively small blocks and allocating
the LLM. Since the model weights are constant and the ac-                                      them on demand. Moreover, it eliminates external fragmen-
tivations only occupy a small fraction of the GPU memory,                                      tation as all blocks have the same size. Finally, it enables
the way the KV cache is managed is critical in determining                                     memory sharing at the granularity of a block, across the
the maximum batch size. When managed inefficiently, the                                        different sequences associated with the same request or even
KV cache memory can significantly limit the batch size and                                     across the different requests.
consequently the throughput of the LLM, as illustrated in                                         In this work, we build vLLM, a high-throughput distributed
Fig. 1 (right).                                                                                LLM serving engine on top of PagedAttention that achieves
   In this paper, we observe that existing LLM serving sys-                                    near-zero waste in KV cache memory. vLLM uses block-level
tems [31, 60] fall short of managing the KV cache memory                                       memory management and preemptive request scheduling
efficiently. This is mainly because they store the KV cache of                                 that are co-designed with PagedAttention. vLLM supports
a request in contiguous memory space, as most deep learning                                    popular LLMs such as GPT [5], OPT [62], and LLaMA [52]
frameworks [33, 39] require tensors to be stored in contigu-                                   with varying sizes, including the ones exceeding the memory
ous memory. However, unlike the tensors in the traditional                                     capacity of a single GPU. Our evaluations on various models
deep learning workloads, the KV cache has unique charac-                                       and workloads show that vLLM improves the LLM serving
teristics: it dynamically grows and shrinks over time as the                                   throughput by 2-4× compared to the state-of-the-art sys-
model generates new tokens, and its lifetime and length are                                    tems [31, 60], without affecting the model accuracy at all. The
not known a priori. These characteristics make the existing                                    improvements are more pronounced with longer sequences,
systems’ approach significantly inefficient in two ways:                                       larger models, and more complex decoding algorithms (§4.3).
   First, the existing systems [31, 60] suffer from internal and                               In summary, we make the following contributions:
external memory fragmentation. To store the KV cache of                                        • We identify the challenges in memory allocation in serving
a request in contiguous space, they pre-allocate a contigu-                                       LLMs and quantify their impact on serving performance.
ous chunk of memory with the request’s maximum length                                          • We propose PagedAttention, an attention algorithm that
(e.g., 2048 tokens). This can result in severe internal frag-                                     operates on KV cache stored in non-contiguous paged
mentation, since the request’s actual length can be much                                          memory, which is inspired by the virtual memory and
shorter than its maximum length (e.g., Fig. 11). Moreover,                                        paging in OS.
even if the actual length is known a priori, the pre-allocation                                • We design and implement vLLM, a distributed LLM serving
is still inefficient: As the entire chunk is reserved during the                                  engine built on top of PagedAttention.
request’s lifetime, other shorter requests cannot utilize any                                  • We evaluate vLLM on various scenarios and demonstrate
part of the chunk that is currently unused. Besides, external                                     that it substantially outperforms the previous state-of-the-
memory fragmentation can also be significant, since the pre-                                      art solutions such as FasterTransformer [31] and Orca [60].
allocated size can be different for each request. Indeed, our
profiling results in Fig. 2 show that only 20.4% - 38.2% of the                                2   Background
KV cache memory is used to store the actual token states in
the existing systems.                                                                          In this section, we describe the generation and serving pro-
   Second, the existing systems cannot exploit the opportu-                                    cedures of typical LLMs and the iteration-level scheduling
nities for memory sharing. LLM services often use advanced                                     used in LLM serving.
                                                                                           2
2.1   Transformer-Based Large Language Models                                          The prompt phase takes the whole user prompt (𝑥 1, . . . , 𝑥𝑛 )
                                                                                       as input and computes the probability of the first new to-
The task of language modeling is to model the probability
                                                                                       ken 𝑃 (𝑥𝑛+1 | 𝑥 1, . . . , 𝑥𝑛 ). During this process, also gener-
of a list of tokens (𝑥 1, . . . , 𝑥𝑛 ). Since language has a natural
                                                                                       ates the key vectors 𝑘 1, . . . , 𝑘𝑛 and value vectors 𝑣 1, . . . , 𝑣𝑛 .
sequential ordering, it is common to factorize the joint prob-
                                                                                       Since prompt tokens 𝑥 1, . . . , 𝑥𝑛 are all known, the computa-
ability over the whole sequence as the product of conditional
                                                                                       tion of the prompt phase can be parallelized using matrix-
probabilities (a.k.a. autoregressive decomposition [3]):
                                                                                       matrix multiplication operations. Therefore, this phase can
                                                                                       efficiently use the parallelism inherent in GPUs.
      𝑃 (𝑥) = 𝑃 (𝑥 1 ) · 𝑃 (𝑥 2 | 𝑥 1 ) · · · 𝑃 (𝑥𝑛 | 𝑥 1, . . . , 𝑥𝑛−1 ).   (1)
                                                                                       The autoregressive generation phase generates the re-
   Transformers [53] have become the de facto standard ar-                             maining new tokens sequentially. At iteration 𝑡, the model
chitecture for modeling the probability above at a large scale.                        takes one token 𝑥𝑛+𝑡 as input and computes the probability
The most important component of a Transformer-based lan-                               𝑃 (𝑥𝑛+𝑡 +1 | 𝑥 1, . . . , 𝑥𝑛+𝑡 ) with the key vectors 𝑘 1, . . . , 𝑘𝑛+𝑡 and
guage model is its self-attention layers. For an input hidden                          value vectors 𝑣 1, . . . , 𝑣𝑛+𝑡 . Note that the key and value vectors
state sequence (𝑥 1, . . . , 𝑥𝑛 ) ∈ R𝑛×𝑑 , a self-attention layer                      at positions 1 to 𝑛 + 𝑡 − 1 are cached at previous iterations,
first applies linear transformations on each position 𝑖 to get                         only the new key and value vector 𝑘𝑛+𝑡 and 𝑣𝑛+𝑡 are com-
the query, key, and value vectors:                                                     puted at this iteration. This phase completes either when the
                                                                                       sequence reaches a maximum length (specified by users or
                 𝑞𝑖 = 𝑊𝑞 𝑥𝑖 , 𝑘𝑖 = 𝑊𝑘 𝑥𝑖 , 𝑣𝑖 = 𝑊𝑣 𝑥𝑖 .                      (2)       limited by LLMs) or when an end-of-sequence (<eos>) token
                                                                                       is emitted. The computation at different iterations cannot
Then, the self-attention layer computes the attention score                            be parallelized due to the data dependency and often uses
𝑎𝑖 𝑗 by multiplying the query vector at one position with all                          matrix-vector multiplication, which is less efficient. As a re-
the key vectors before it and compute the output 𝑜𝑖 as the                             sult, this phase severely underutilizes GPU computation and
weighted average over the value vectors:                                               becomes memory-bound, being responsible for most portion
                                                                                       of the latency of a single request.
                                 √
                     exp(𝑞𝑖⊤𝑘 𝑗 / 𝑑)         𝑖
                                            ∑︁                                         2.3    Batching Techniques for LLMs
           𝑎𝑖 𝑗 = Í𝑖               √ , 𝑜𝑖 =     𝑎𝑖 𝑗 𝑣 𝑗 .                   (3)
                              ⊤
                   𝑡 =1 exp(𝑞𝑖 𝑘𝑡 / 𝑑)      𝑗=1                                        The compute utilization in serving LLMs can be improved
                                                                                       by batching multiple requests. Because the requests share
   Besides the computation in Eq. 4, all other components                              the same model weights, the overhead of moving weights is
in the Transformer model, including the embedding layer,                               amortized across the requests in a batch, and can be over-
feed-forward layer, layer normalization [2], residual connec-                          whelmed by the computational overhead when the batch
tion [22], output logit computation, and the query, key, and                           size is sufficiently large. However, batching the requests
value transformation in Eq. 2, are all applied independently                           to an LLM service is non-trivial for two reasons. First, the
position-wise in a form of 𝑦𝑖 = 𝑓 (𝑥𝑖 ).                                               requests may arrive at different times. A naive batching strat-
                                                                                       egy would either make earlier requests wait for later ones
2.2   LLM Service & Autoregressive Generation
                                                                                       or delay the incoming requests until earlier ones finish, lead-
Once trained, LLMs are often deployed as a conditional gen-                            ing to significant queueing delays. Second, the requests may
eration service (e.g., completion API [34] or chatbot [19, 35]).                       have vastly different input and output lengths (Fig. 11). A
A request to an LLM service provides a list of input prompt                            straightforward batching technique would pad the inputs
tokens (𝑥 1, . . . , 𝑥𝑛 ), and the LLM service generates a list of                     and outputs of the requests to equalize their lengths, wasting
output tokens (𝑥𝑛+1, . . . , 𝑥𝑛+𝑇 ) according to Eq. 1. We refer to                    GPU computation and memory.
the concatenation of the prompt and output lists as sequence.                             To address this problem, fine-grained batching mecha-
   Due to the decomposition in Eq. 1, the LLM can only sam-                            nisms, such as cellular batching [16] and iteration-level sched-
ple and generate new tokens one by one, and the generation                             uling [60], have been proposed. Unlike traditional methods
process of each new token depends on all the previous tokens                           that work at the request level, these techniques operate at
in that sequence, specifically their key and value vectors. In                         the iteration level. After each iteration, completed requests
this sequential generation process, the key and value vectors                          are removed from the batch, and new ones are added. There-
of existing tokens are often cached for generating future                              fore, a new request can be processed after waiting for a
tokens, known as KV cache. Note that the KV cache of one                               single iteration, not waiting for the entire batch to complete.
token depends on all its previous tokens. This means that the                          Moreover, with special GPU kernels, these techniques elim-
KV cache of the same token appearing at different positions                            inate the need to pad the inputs and outputs. By reducing
in a sequence will be different.                                                       the queueing delay and the inefficiencies from padding, the
   Given a request prompt, the generation computation in                               fine-grained batching mechanisms significantly increase the
the LLM service can be decomposed into two phases:                                     throughput of LLM serving.
                                                                                   3
                                                           1 slot for      2 slots future used                                                                 1 slot future used
                                                        generated token        (reserved)                         External fragmentation                           (reserved)


          Four   score   and    seven   years    ago   our   fathers brought forth   <eos> <resv>       …    <resv>                    You    only    live    once   <eos> <resv>     …     <resv>


                         7 KV cache states for                                                2038 slots never used                   3 KV cache states for                   507 slots never used
                          request A’s prompt                                                 (internal fragmentation)                  request B’s prompt                   (Internal fragmentation)
                                                                  Request A                                                                               Request B
                                                                current iteration                                                                       current iteration


Figure 3. KV cache memory management in existing systems. Three types of memory wastes – reserved, internal fragmentation,
and external fragmentation – exist that prevent other requests from fitting into the memory. The token in each memory slot
represents its KV cache. Note the same tokens can have different KV cache when at different positions.

3   Memory Challenges in LLM Serving                                                                        §6.3) of their KV cache, and the sharing pattern evolves as
                                                                                                            the decoding process advances.
Although fine-grained batching reduces the waste of com-                                                    Scheduling for unknown input & output lengths. The
puting and enables requests to be batched in a more flexible                                                requests to an LLM service exhibit variability in their input
way, the number of requests that can be batched together is                                                 and output lengths. This requires the memory management
still constrained by GPU memory capacity, particularly the                                                  system to accommodate a wide range of prompt lengths. In
space allocated to store the KV cache. In other words, the                                                  addition, as the output length of a request grows at decoding,
serving system’s throughput is memory-bound. Overcom-                                                       the memory required for its KV cache also expands and may
ing this memory-bound requires addressing the following                                                     exhaust available memory for incoming requests or ongoing
challenges in the memory management:                                                                        generation for existing prompts. The system needs to make
Large KV cache. The KV Cache size grows quickly with the                                                    scheduling decisions, such as deleting or swapping out the
number of requests. As an example, for the 13B parameter                                                    KV cache of some requests from GPU memory.
OPT model [62], the KV cache of a single token demands 800
KB of space, calculated as 2 (key and value vectors) × 5120
                                                                                                            3.1         Memory Management in Existing Systems
(hidden state size) × 40 (number of layers) × 2 (bytes per
FP16). Since OPT can generate sequences up to 2048 tokens,                                                  Since most operators in current deep learning frameworks
the memory required to store the KV cache of one request                                                    [33, 39] require tensors to be stored in contiguous memory,
can be as much as 1.6 GB. Concurrent GPUs have memory                                                       previous LLM serving systems [31, 60] also store the KV
capacities in the tens of GBs. Even if all available memory                                                 cache of one request as a contiguous tensor across the differ-
was allocated to KV cache, only a few tens of requests could                                                ent positions. Due to the unpredictable output lengths from
be accommodated. Moreover, inefficient memory manage-                                                       the LLM, they statically allocate a chunk of memory for a
ment can further decrease the batch size, as shown in Fig. 2.                                               request based on the request’s maximum possible sequence
Additionally, given the current trends, the GPU’s computa-                                                  length, irrespective of the actual input or eventual output
tion speed grows faster than the memory capacity [17]. For                                                  length of the request.
example, from NVIDIA A100 to H100, The FLOPS increases                                                         Fig. 3 illustrates two requests: request A with 2048 max-
by more than 2x, but the GPU memory stays at 80GB max-                                                      imum possible sequence length and request B with a max-
imum. Therefore, we believe the memory will become an                                                       imum of 512. The chunk pre-allocation scheme in existing
increasingly significant bottleneck.                                                                        systems has three primary sources of memory wastes: re-
Complex decoding algorithms. LLM services offer a range                                                     served slots for future tokens, internal fragmentation due to
of decoding algorithms for users to select from, each with                                                  over-provisioning for potential maximum sequence lengths,
varying implications for memory management complexity.                                                      and external fragmentation from the memory allocator like
For example, when users request multiple random samples                                                     the buddy allocator. The external fragmentation will never
from a single input prompt, a typical use case in program                                                   be used for generated tokens, which is known before serving
suggestion [18], the KV cache of the prompt part, which                                                     a request. Internal fragmentation also remains unused, but
accounts for 12% of the total KV cache memory in our ex-                                                    this is only realized after a request has finished sampling.
periment (§6.3), can be shared to minimize memory usage.                                                    They are both pure memory waste. Although the reserved
On the other hand, the KV cache during the autoregressive                                                   memory is eventually used, reserving this space for the en-
generation phase should remain unshared due to the dif-                                                     tire request’s duration, especially when the reserved space
ferent sample results and their dependence on context and                                                   is large, occupies the space that could otherwise be used to
position. The extent of KV cache sharing depends on the                                                     process other requests. We visualize the average percentage
specific decoding algorithm employed. In more sophisticated                                                 of memory wastes in our experiments in Fig. 2, revealing
algorithms like beam search [49], different request beams                                                   that the actual effective memory in previous systems can be
can share larger portions (up to 55% memory saving, see                                                     as low as 20.4%.
                                                                                                    4
                                                                                                                                    Key and value vectors
                                         Worker 0
              Scheduler                     Cache         Model                                                   Block 1   years       ago      our    fathers
                                            Engine       Shard 0


                                         Worker 1                                                                 Block 2   brought     forth
         KV Cache Manager                                                                  Query
                                                                                                    forth
                                            Cache         Model                            vector
                                            Engine       Shard 1


             Block tables
                                                        …
                                                                                                                  Block 0    Four       score    and    seven
                                         Worker N - 1
      CPU Block       GPU Block             Cache         Model
       Allocator       Allocator            Engine      Shard N - 1
                                                                                    Figure 5. Illustration of the PagedAttention algorithm,
                                                                                    where the attention key and values vectors are stored as
                   Figure 4. vLLM system overview.                                  non-contiguous blocks in the memory.

   Although compaction [54] has been proposed as a poten-                           block size (𝐵). Denote the key block 𝐾 𝑗 = (𝑘 ( 𝑗 −1)𝐵+1, . . . , 𝑘 𝑗𝐵 )
tial solution to fragmentation, performing compaction in a                          and value block 𝑉𝑗 = (𝑣 ( 𝑗 −1)𝐵+1, . . . , 𝑣 𝑗𝐵 ). The attention com-
performance-sensitive LLM serving system is impractical                             putation in Eq. 4 can be transformed into the following block-
due to the massive KV cache. Even with compaction, the                              wise computation:
pre-allocated chunk space for each request prevents memory                                                          √                    ⌈𝑖/𝐵
                                                                                                        exp(𝑞𝑖⊤𝐾 𝑗 / 𝑑)                   ∑︁⌉
sharing specific to decoding algorithms in existing memory                                 𝐴𝑖 𝑗 = Í ⌈𝑖/𝐵 ⌉              √ , 𝑜𝑖 =              𝑉𝑗 𝐴𝑖⊤𝑗 ,  (4)
management systems.                                                                                        exp(𝑞 ⊤ 𝐾 1/ 𝑑)
                                                                                                     𝑡 =1        𝑖 𝑡                      𝑗=1

4     Method                                                                        where 𝐴𝑖 𝑗 = (𝑎𝑖,( 𝑗 −1)𝐵+1, . . . , 𝑎𝑖,𝑗𝐵 ) is the row vector of atten-
In this work, we develop a new attention algorithm, Page-                           tion score on 𝑗-th KV block.
dAttention, and build an LLM serving engine, vLLM, to tackle                           During the attention computation, the PagedAttention
the challenges outlined in §3. The architecture of vLLM is                          kernel identifies and fetches different KV blocks separately.
shown in Fig. 4. vLLM adopts a centralized scheduler to                             We show an example of PagedAttention in Fig. 5: The key
coordinate the execution of distributed GPU workers. The                            and value vectors are spread across three blocks, and the
KV cache manager effectively manages the KV cache in a                              three blocks are not contiguous on the physical memory. At
paged fashion, enabled by PagedAttention. Specifically, the                         each time, the kernel multiplies the query vector 𝑞𝑖 of the
KV cache manager manages the physical KV cache memory                               query token (“forth”) and the key vectors 𝐾 𝑗 in a block (e.g.,
on the GPU workers through the instructions sent by the                             key vectors of “Four score and seven” for block 0) to compute
centralized scheduler.                                                              the attention score 𝐴𝑖 𝑗 , and later multiplies 𝐴𝑖 𝑗 with the value
   Next, We describe the PagedAttention algorithm in §4.1.                          vectors 𝑉𝑗 in a block to derive the final attention output 𝑜𝑖 .
With that, we show the design of the KV cache manager in                               In summary, the PagedAttention algorithm allows the
§4.2 and how it facilitates PagedAttention in §4.3, respec-                         KV blocks to be stored in non-contiguous physical memory,
tively. Then, we show how this design facilitates effective                         which enables more flexible paged memory management in
memory management for various decoding methods (§4.4)                               vLLM.
and handles the variable length input and output sequences                          4.2   KV Cache Manager
(§4.5). Finally, we show how the system design of vLLM                              The key idea behind vLLM’s memory manager is analogous
works in a distributed setting (§4.6).                                              to the virtual memory [25] in operating systems. OS parti-
4.1    PagedAttention                                                               tions memory into fixed-sized pages and maps user programs’
To address the memory challenges in §3, we introduce Page-                          logical pages to physical pages. Contiguous logical pages can
dAttention, an attention algorithm inspired by the classic idea                     correspond to non-contiguous physical memory pages, al-
of paging [25] in operating systems. Unlike the traditional                         lowing user programs to access memory as though it were
attention algorithms, PagedAttention allows storing continu-                        contiguous. Moreover, physical memory space needs not to
ous keys and values in non-contiguous memory space. Specif-                         be fully reserved in advance, enabling the OS to dynamically
ically, PagedAttention partitions the KV cache of each se-                          allocate physical pages as needed. vLLM uses the ideas be-
quence into KV blocks. Each block contains the key and value                        hind virtual memory to manage the KV cache in an LLM
vectors for a fixed number of tokens,1 which we denote as KV                        service. Enabled by PagedAttention, we organize the KV
                                                                                    cache as fixed-size KV blocks, like pages in virtual memory.
1 In Transformer, each token has a set of key and value vectors across layers
                                                                                       A request’s KV cache is represented as a series of logical
and attention heads within a layer. All the key and value vectors can be            KV blocks, filled from left to right as new tokens and their KV
managed together within a single KV block, or the key and value vectors at
different heads and layers can each have a separate block and be managed            cache are generated. The last KV block’s unfilled positions
in separate block tables. The two designs have no performance difference            are reserved for future generations. On GPU workers, a block
and we choose the second one for easy implementation.                               engine allocates a contiguous chunk of GPU DRAM and
                                                                                5
                                                                                                                     Physical KV blocks                                                                                     Physical KV blocks
                                                                                                                      (on GPU DRAM)
                                                                                                                                                                                                          Block 0
                                                                                                                                                                                 Request                                                                                     Request
                         Prompt: “Four score and seven years ago our”                          Block 0                                                                             A                                                                                           B
          Request                                                                                                                                                                                         Block 1   years     ago      our   fathers
            A            Outputs: “fathers” → “brought” → …                                              1            1           1         2
                                                                                               Block 1       years        ago         our   fathers
                                                                                                                                                                            Logical KV blocks             Block 2    of       times                                     Logical KV blocks

                        Logical KV blocks                                                      Block 2                                                    Block 0   Four     score     and      seven     Block 3 brought                                Block 0   It     was      the      best
            1            1         1         1                 Block Table                               3
Block 0         Four     score         and   seven                                     1       Block 3 brought                                            Block 1   years     ago      our      fathers   Block 4                                        Block 1   of    times
                                                           Physical block
                                                       1                    # filled
            1            1         1         2                number                                                                                      Block 2 brought                                                                                Block 2
Block 1         years        ago       our   fathers                                       3                                                                                                              Block 5    It       was      the       best
                                                       1
                                                               1 7           14                Block 4
            3                                                  1 1          1 3→4 2                                                                       Block 3                                         Block 6
Block 2 brought                                        3                                       Block 5
                                                               3 3           31
                                                                                       1                                                                                                                  Block 7   Four      score    and       seven
Block 3                                                          –             –
                                                                                               Block 6
                                                                                                                                                                                                          Block 8
                                                                                                         1            1           1         1
                                                                                               Block 7       Four         score       and   seven

                                                                                               Block 8
                                                                                                                                                          Figure 7. Storing the KV cache of two requests at the same
                                                                                                                                                          time in vLLM.
                        Figure 6. Block table translation in vLLM.

divides it into physical KV blocks (this is also done on CPU                                                                                              requests and the latest tokens for generation phase requests)
RAM for swapping; see §4.5). The KV block manager also                                                                                                    as one sequence and feeds it into the LLM. During LLM’s
maintains block tables—the mapping between logical and                                                                                                    computation, vLLM uses the PagedAttention kernel to access
physical KV blocks of each request. Each block table entry                                                                                                the previous KV cache stored in the form of logical KV blocks
records the corresponding physical blocks of a logical block                                                                                              and saves the newly generated KV cache into the physical
and the number of filled positions. Separating logical and                                                                                                KV blocks. Storing multiple tokens within a KV block (block
physical KV blocks allows vLLM to dynamically grow the                                                                                                    size > 1) enables the PagedAttention kernel to process the
KV cache memory without reserving it for all positions in                                                                                                 KV cache across more positions in parallel, thus increasing
advance, which eliminates most memory waste in existing                                                                                                   the hardware utilization and reducing latency. However, a
systems, as in Fig. 2.                                                                                                                                    larger block size also increases memory fragmentation. We
                                                                                                                                                          study the effect of block size in §7.2.
4.3             Decoding with PagedAttention and vLLM                                                                                                        Again, vLLM dynamically assigns new physical blocks to
Next, we walk through an example, as in Fig. 6, to demon-                                                                                                 logical blocks as more tokens and their KV cache are gener-
strate how vLLM executes PagedAttention and manages the                                                                                                   ated. As all the blocks are filled from left to right and a new
memory during the decoding process of a single input se-                                                                                                  physical block is only allocated when all previous blocks
quence: ○ 1 As in OS’s virtual memory, vLLM does not require                                                                                              are full, vLLM limits all the memory wastes for a request
reserving the memory for the maximum possible generated                                                                                                   within one block, so it can effectively utilize all the memory,
sequence length initially. Instead, it reserves only the nec-                                                                                             as shown in Fig. 2. This allows more requests to fit into mem-
essary KV blocks to accommodate the KV cache generated                                                                                                    ory for batching—hence improving the throughput. Once a
during prompt computation. In this case, The prompt has 7                                                                                                 request finishes its generation, its KV blocks can be freed to
tokens, so vLLM maps the first 2 logical KV blocks (0 and                                                                                                 store the KV cache of other requests. In Fig. 7, we show an
1) to 2 physical KV blocks (7 and 1, respectively). In the                                                                                                example of vLLM managing the memory for two sequences.
prefill step, vLLM generates the KV cache of the prompts                                                                                                  The logical blocks of the two sequences are mapped to differ-
and the first output token with a conventional self-attention                                                                                             ent physical blocks within the space reserved by the block
algorithm (e.g., [13]). vLLM then stores the KV cache of the                                                                                              engine in GPU workers. The neighboring logical blocks of
first 4 tokens in logical block 0 and the following 3 tokens                                                                                              both sequences do not need to be contiguous in physical GPU
in logical block 1. The remaining slot is reserved for the                                                                                                memory and the space of physical blocks can be effectively
subsequent autoregressive generation phase. ○     2 In the first                                                                                          utilized by both sequences.
autoregressive decoding step, vLLM generates the new token                                                                                                4.4         Application to Other Decoding Scenarios
with the PagedAttention algorithm on physical blocks 7 and
1. Since one slot remains available in the last logical block,                                                                                            §4.3 shows how PagedAttention and vLLM handle basic de-
the newly generated KV cache is stored there, and the block                                                                                               coding algorithms, such as greedy decoding and sampling,
table’s #filled record is updated. ○ 3 At the second decoding                                                                                             that take one user prompt as input and generate a single out-
step, as the last logical block is full, vLLM stores the newly                                                                                            put sequence. In many successful LLM applications [18, 34],
generated KV cache in a new logical block; vLLM allocates a                                                                                               an LLM service must offer more complex decoding scenarios
new physical block (physical block 3) for it and stores this                                                                                              that exhibit complex accessing patterns and more opportuni-
mapping in the block table.                                                                                                                               ties for memory sharing. We show the general applicability
   Globally, for each decoding iteration, vLLM first selects                                                                                              of vLLM on them in this section.
a set of candidate sequences for batching (more in §4.5),                                                                                                 Parallel sampling. In LLM-based program assistants [6, 18],
and allocates the physical blocks for the newly required                                                                                                  an LLM generates multiple sampled outputs for a single in-
logical blocks. Then, vLLM concatenates all the input tokens                                                                                              put prompt; users can choose a favorite output from various
of the current iteration (i.e., all tokens for prompt phase                                                                                               candidates. So far we have implicitly assumed that a request
                                                                                                                                                      6
                                                                  Physical KV blocks

                                                Block 0                                                                                                         Beam candidate 0                                   Block 5   Block 9
                                                                                                 Ref count: 2 → 1
                       Sample                                                                                                   Sample
                         A1                     Block 1   years     ago      our   mothers                                        A2


                  Logical KV blocks             Block 2 Copy-on-write                                                      Logical KV blocks                    Beam candidate 1     Block 0   Block 1   Block 3   Block 6   Block 10

Block 0   Four     score     and      seven     Block 3   years     ago      our       fathers       Block 0        Four    score     and      seven
                                                                                                                                                                Beam candidate 2                                   Block 7   Block 11
Block 1   years     ago      our      fathers   Block 4                                              Block 1    years        ago      our      mothers

                                                Block 5
                                                                                                                                                                Beam candidate 3               Block 2   Block 4   Block 8   Block 12
                                                Block 6

                                                Block 7   Four     score     and       seven

                                                Block 8                                                                                                                            Figure 9. Beam search example.

                           Figure 8. Parallel sampling example.                                                                                              sample space. The algorithm relies on the beam width pa-
                                                                                                                                                             rameter 𝑘, which determines the number of top candidates
generates a single sequence. In the remainder of this paper,                                                                                                 retained at every step. During decoding, beam search ex-
we assume the more general case in which a request gener-                                                                                                    pands each candidate sequence in the beam by considering
ates multiple sequences. In parallel sampling, one request                                                                                                   all possible tokens, computes their respective probabilities us-
includes multiple samples sharing the same input prompt,                                                                                                     ing the LLM, and retains the top-𝑘 most probable sequences
allowing the KV cache of the prompt to be shared as well. Via                                                                                                out of 𝑘 · |𝑉 | candidates, where |𝑉 | is the vocabulary size.
its PagedAttention and paged memory management, vLLM                                                                                                            Unlike parallel decoding, beam search facilities sharing
can realize this sharing easily and save memory.                                                                                                             not only the initial prompt blocks but also other blocks across
   Fig. 8 shows an example of parallel decoding for two out-                                                                                                 different candidates, and the sharing patterns dynamically
puts. Since both outputs share the same prompt, we only                                                                                                      change as the decoding process advances, similar to the pro-
reserve space for one copy of the prompt’s state at the prompt                                                                                               cess tree in the OS created by compound forks. Fig. 9 shows
phase; the logical blocks for the prompts of both sequences                                                                                                  how vLLM manages the KV blocks for a beam search ex-
are mapped to the same physical blocks: the logical block 0                                                                                                  ample with 𝑘 = 4. Prior to the iteration illustrated as the
and 1 of both sequences are mapped to physical blocks 7 and                                                                                                  dotted line, each candidate sequence has used 4 full logi-
1, respectively. Since a single physical block can be mapped                                                                                                 cal blocks. All beam candidates share the first block 0 (i.e.,
to multiple logical blocks, we introduce a reference count for                                                                                               prompt). Candidate 3 digresses from others from the second
each physical block. In this case, the reference counts for                                                                                                  block. Candidates 0-2 share the first 3 blocks and diverge at
physical blocks 7 and 1 are both 2. At the generation phase,                                                                                                 the fourth block. At subsequent iterations, the top-4 prob-
the two outputs sample different output tokens and need                                                                                                      able candidates all originate from candidates 1 and 2. As
separate storage for KV cache. vLLM implements a copy-on-                                                                                                    the original candidates 0 and 3 are no longer among the
write mechanism at the block granularity for the physical                                                                                                    top candidates, their logical blocks are freed, and the refer-
blocks that need modification by multiple sequences, similar                                                                                                 ence counts of corresponding physical blocks are reduced.
to the copy-on-write technique in OS virtual memory (e.g.,                                                                                                   vLLM frees all physical blocks whose reference counts reach
when forking a process). Specifically, in Fig. 8, when sample                                                                                                0 (blocks 2, 4, 5, 8). Then, vLLM allocates new physical blocks
A1 needs to write to its last logical block (logical block 1),                                                                                               (blocks 9-12) to store the new KV cache from the new can-
vLLM recognizes that the reference count of the correspond-                                                                                                  didates. Now, all candidates share blocks 0, 1, 3; candidates
ing physical block (physical block 1) is greater than 1; it                                                                                                  0 and 1 share block 6, and candidates 2 and 3 further share
allocates a new physical block (physical block 3), instructs                                                                                                 block 7.
the block engine to copy the information from physical block                                                                                                    Previous LLM serving systems require frequent memory
1, and decreases the reference count to 1. Next, when sample                                                                                                 copies of the KV cache across the beam candidates. For exam-
A2 writes to physical block 1, the reference count is already                                                                                                ple, in the case shown in Fig. 9, after the dotted line, candidate
reduced to 1; thus A2 directly writes its newly generated KV                                                                                                 3 would need to copy a large portion of candidate 2’s KV
cache to physical block 1.                                                                                                                                   cache to continue generation. This frequent memory copy
   In summary, vLLM enables the sharing of most of the                                                                                                       overhead is significantly reduced by vLLM’s physical block
space used to store the prompts’ KV cache across multiple                                                                                                    sharing. In vLLM, most blocks of different beam candidates
output samples, with the exception of the final logical block,                                                                                               can be shared. The copy-on-write mechanism is applied only
which is managed by a copy-on-write mechanism. By sharing                                                                                                    when the newly generated tokens are within an old shared
physical blocks across multiple samples, memory usage can                                                                                                    block, as in parallel decoding. This involves only copying
be greatly reduced, especially for long input prompts.                                                                                                       one block of data.
Beam search. In LLM tasks like machine translation [59],                                                                                                     Shared prefix. Commonly, the LLM user provides a (long)
the users expect the top-𝑘 most appropriate translations out-                                                                                                description of the task including instructions and example
put by the LLM. Beam search [49] is widely used to decode                                                                                                    inputs and outputs, also known as system prompt [36]. The
the most probable output sequence from an LLM, as it miti-                                                                                                   description is concatenated with the actual task input to form
gates the computational complexity of fully traversing the                                                                                                   the prompt of the request. The LLM generates outputs based
                                                                                                                                                         7
                                  Sequence A                              Sequence B
                                    Prompt                                  Prompt                      context: (1) Which blocks should it evict? (2) How to recover
                    Translate English to French:            Translate English to French:                evicted blocks if needed again? Typically, eviction policies
                    “sea otter” => “loutre de mer”          “sea otter” => “loutre de mer”
   Shared prefix    “peppermint” => “menthe poivrée”
                    “plush girafe” => “girafe en peluche”
                                                            “peppermint” => “menthe poivrée”
                                                            “plush girafe” => “girafe en peluche”
                                                                                                        use heuristics to predict which block will be accessed fur-
       Task input   “cheese” =>                             “I love you” =>
                                                                                                        thest in the future and evict that block. Since in our case we
                                  Sequence A                              Sequence B                    know that all blocks of a sequence are accessed together, we
                                  LLM output                              LLM output
      Task output   “fromage”                               “Je t’amie”
                                                                                                        implement an all-or-nothing eviction policy, i.e., either evict
                                                                                                        all or none of the blocks of a sequence. Furthermore, multi-
Figure 10. Shared prompt example for machine translation.                                               ple sequences within one request (e.g., beam candidates in
The examples are adopted from [5].                                                                      one beam search request) are gang-scheduled as a sequence
                                                                                                        group. The sequences within one sequence group are always
on the full prompt. Fig. 10 shows an example. Moreover, the                                             preempted or rescheduled together due to potential memory
shared prefix can be further tuned, via prompt engineering,                                             sharing across those sequences. To answer the second ques-
to improve the accuracy of the downstream tasks [26, 27].                                               tion of how to recover an evicted block, we consider two
   For this type of application, many user prompts share a                                              techniques:
prefix, thus the LLM service provider can store the KV cache
                                                                                                        Swapping. This is the classic technique used by most virtual
of the prefix in advance to reduce the redundant computa-
                                                                                                        memory implementations which copy the evicted pages to a
tion spent on the prefix. In vLLM, this can be conveniently
                                                                                                        swap space on the disk. In our case, we copy evicted blocks to
achieved by reserving a set of physical blocks for a set of
                                                                                                        the CPU memory. As shown in Fig. 4, besides the GPU block
predefined shared prefixes by the LLM service provider, as
                                                                                                        allocator, vLLM includes a CPU block allocator to manage
how OS handles shared library across processes. A user in-
                                                                                                        the physical blocks swapped to CPU RAM. When vLLM
put prompt with the shared prefix can simply map its logi-
                                                                                                        exhausts free physical blocks for new tokens, it selects a set
cal blocks to the cached physical blocks (with the last block
                                                                                                        of sequences to evict and transfer their KV cache to the CPU.
marked copy-on-write). The prompt phase computation only
                                                                                                        Once it preempts a sequence and evicts its blocks, vLLM
needs to execute on the user’s task input.
                                                                                                        stops accepting new requests until all preempted sequences
Mixed decoding methods. The decoding methods dis-                                                       are completed. Once a request completes, its blocks are freed
cussed earlier exhibit diverse memory sharing and access-                                               from memory, and the blocks of a preempted sequence are
ing patterns. Nonetheless, vLLM facilitates the simultane-                                              brought back in to continue the processing of that sequence.
ous processing of requests with different decoding prefer-                                              Note that with this design, the number of blocks swapped to
ences, which existing systems cannot efficiently do. This is                                            the CPU RAM never exceeds the number of total physical
because vLLM conceals the complex memory sharing be-                                                    blocks in the GPU RAM, so the swap space on the CPU RAM
tween different sequences via a common mapping layer that                                               is bounded by the GPU memory allocated for the KV cache.
translates logical blocks to physical blocks. The LLM and
                                                                                                        Recomputation. In this case, we simply recompute the KV
its execution kernel only see a list of physical block IDs
                                                                                                        cache when the preempted sequences are rescheduled. Note
for each sequence and do not need to handle sharing pat-
                                                                                                        that recomputation latency can be significantly lower than
terns across sequences. Compared to existing systems, this
                                                                                                        the original latency, as the tokens generated at decoding
approach broadens the batching opportunities for requests
                                                                                                        can be concatenated with the original user prompt as a new
with different sampling requirements, ultimately increasing
                                                                                                        prompt—their KV cache at all positions can be generated in
the system’s overall throughput.
                                                                                                        one prompt phase iteration.
4.5     Scheduling and Preemption                                                                          The performances of swapping and recomputation depend
When the request traffic surpasses the system’s capacity,                                               on the bandwidth between CPU RAM and GPU memory and
vLLM must prioritize a subset of requests. In vLLM, we adopt                                            the computation power of the GPU. We examine the speeds
the first-come-first-serve (FCFS) scheduling policy for all                                             of swapping and recomputation in §7.3.
requests, ensuring fairness and preventing starvation. When
                                                                                                        4.6   Distributed Execution
vLLM needs to preempt requests, it ensures that the earliest
arrived requests are served first and the latest requests are                                           Many LLMs have parameter sizes exceeding the capacity of a
preempted first.                                                                                        single GPU [5, 9]. Therefore, it is necessary to partition them
   LLM services face a unique challenge: the input prompts                                              across distributed GPUs and execute them in a model parallel
for an LLM can vary significantly in length, and the resulting                                          fashion [28, 63]. This calls for a memory manager capable of
output lengths are not known a priori, contingent on both                                               handling distributed memory. vLLM is effective in distributed
the input prompt and the model. As the number of requests                                               settings by supporting the widely used Megatron-LM style
and their outputs grow, vLLM can run out of the GPU’s phys-                                             tensor model parallelism strategy on Transformers [47]. This
ical blocks to store the newly generated KV cache. There                                                strategy adheres to an SPMD (Single Program Multiple Data)
are two classic questions that vLLM needs to answer in this                                             execution schedule, wherein the linear layers are partitioned
                                                                                                    8
      Table 1. Model sizes and server configurations.                            2.0
                                                                                       1e−2
                                                                                                                                        8
                                                                                                                                            1e−2

                                                                                                 Input (mean: 161.31)                                    Input (mean: 19.31)
      Model size              13B      66B        175B                           1.5             Output (mean: 337.99)                  6                Output (mean: 58.45)




                                                                       Density




                                                                                                                              Density
      GPUs                    A100    4×A100   8×A100-80GB                       1.0                                                    4
      Total GPU memory        40 GB   160 GB     640 GB
      Parameter size          26 GB   132 GB     346 GB                          0.5                                                    2


      Memory for KV cache     12 GB   21 GB      264 GB                          0.0                                                    0
                                                                                        0      500     1000     1500   2000                 0      500     1000     1500   2000
      Max. # KV cache slots   15.7K    9.7K       60.1K                                              # Tokens                                            # Tokens

                                                                                              (a) ShareGPT                                         (b) Alpaca
to perform block-wise matrix multiplication, and the the              Figure 11. Input and output length distributions of the (a)
GPUs constantly synchronize intermediate results via an all-          ShareGPT and (b) Alpaca datasets.
reduce operation. Specifically, the attention operator is split
on the attention head dimension, each SPMD process takes              PyTorch [39] and Transformers [58]. We use NCCL [32] for
care of a subset of attention heads in multi-head attention.          tensor communication across the distributed GPU workers.
   We observe that even with model parallel execution, each
model shard still processes the same set of input tokens, thus        5.1              Kernel-level Optimization
requiring the KV Cache for the same positions. Therefore,             Since PagedAttention introduces memory access patterns
vLLM features a single KV cache manager within the cen-               that are not efficiently supported by existing systems, we
tralized scheduler, as in Fig. 4. Different GPU workers share         develop several GPU kernels for optimizing it. (1) Fused re-
the manager, as well as the mapping from logical blocks to            shape and block write. In every Transformer layer, the new
physical blocks. This common mapping allows GPU workers               KV cache are split into blocks, reshaped to a memory layout
to execute the model with the physical blocks provided by             optimized for block read, then saved at positions specified
the scheduler for each input request. Although each GPU               by the block table. To minimize kernel launch overheads, we
worker has the same physical block IDs, a worker only stores          fuse them into a single kernel. (2) Fusing block read and atten-
a portion of the KV cache for its corresponding attention             tion. We adapt the attention kernel in FasterTransformer [31]
heads.                                                                to read KV cache according to the block table and perform
   In each step, the scheduler first prepares the message with        attention operations on the fly. To ensure coalesced memory
input token IDs for each request in the batch, as well as the         access, we assign a GPU warp to read each block. More-
block table for each request. Next, the scheduler broadcasts          over, we add support for variable sequence lengths within a
this control message to the GPU workers. Then, the GPU                request batch. (3) Fused block copy. Block copy operations,
workers start to execute the model with the input token IDs.          issued by the copy-on-write mechanism, may operate on
In the attention layers, the GPU workers read the KV cache            discontinuous blocks. This can lead to numerous invocations
according to the block table in the control message. During           of small data movements if we use the cudaMemcpyAsync
execution, the GPU workers synchronize the intermediate               API. To mitigate the overhead, we implement a kernel that
results with the all-reduce communication primitive without           batches the copy operations for different blocks into a single
the coordination of the scheduler, as in [47]. In the end, the        kernel launch.
GPU workers send the sampled tokens of this iteration back
                                                                      5.2              Supporting Various Decoding Algorithms
to the scheduler. In summary, GPU workers do not need
to synchronize on memory management as they only need                 vLLM implements various decoding algorithms using three
to receive all the memory management information at the               key methods: fork, append, and free. The fork method
beginning of each decoding iteration along with the step              creates a new sequence from an existing one. The append
inputs.                                                               method appends a new token to the sequence. Finally, the
                                                                      free method deletes the sequence. For instance, in paral-
5   Implementation
                                                                      lel sampling, vLLM creates multiple output sequences from
vLLM is an end-to-end serving system with a FastAPI [15]              the single input sequence using the fork method. It then
frontend and a GPU-based inference engine. The frontend               adds new tokens to these sequences in every iteration with
extends the OpenAI API [34] interface, allowing users to              append, and deletes sequences that meet a stopping condi-
customize sampling parameters for each request, such as               tion using free. The same strategy is also applied in beam
the maximum sequence length and the beam width 𝑘. The                 search and prefix sharing by vLLM. We believe future decod-
vLLM engine is written in 8.5K lines of Python and 2K lines of        ing algorithms can also be supported by combining these
C++/CUDA code. We develop control-related components in-              methods.
cluding the scheduler and the block manager in Python while
developing custom CUDA kernels for key operations such as             6            Evaluation
PagedAttention. For the model executor, we implement pop-             In this section, we evaluate the performance of vLLM under
ular LLMs such as GPT [5], OPT [62], and LLaMA [52] using             a variety of workloads.
                                                                  9
                                                              FasterTransformer                                        Orca (Max)              Orca (Pow2)         Orca (Oracle)              vLLM
 Normalized latency



                                 1.0                                                                             1.0                                                1.0
    (s/token)




                                 0.5                                                                             0.5                                                0.5

                                 0.0                                                                             0.0                                                0.0
                                   0.0             0.5     1.0        1.5                               2.0        0.0        0.2      0.4     0.6    0.8    1.0      0.0      0.5       1.0    1.5    2.0    2.5
                                                     Request rate (req/s)                                                            Request rate (req/s)                              Request rate (req/s)

                                           (a) OPT-13B, 1 GPU, ShareGPT                                                     (b) OPT-66B, 4 GPUs, ShareGPT                     (c) OPT-175B, 8 GPUs, ShareGPT
Normalized latency




                                 1.0                                                                             1.0                                                1.0
   (s/token)




                                 0.5                                                                             0.5                                                0.5

                                 0.0                                                                             0.0                                                0.0
                                       0             10           20                                    30             0            5       10        15      20          0        5        10       15       20
                                                    Request rate (req/s)                                                             Request rate (req/s)                              Request rate (req/s)

                                             (d) OPT-13B, 1 GPU, Alpaca                                                      (e) OPT-66B, 4 GPUs, Alpaca                       (f) OPT-175B, 8 GPUs, Alpaca

                                              Figure 12. Single sequence generation with OPT models on the ShareGPT and Alpaca dataset
                                                                                          150
                            35
                                                             30.42                                                         132.44             As FasterTransformer does not have its own scheduler, we
                                                                     # Batched requests




                            30                                                            125
       # Batched requests




                            25
                                                                                                                                              implement a custom scheduler with a dynamic batching
                                                                                          100
                            20
                                                                                          75                      72.75                       mechanism similar to the existing serving systems such as
                                                     13.62
                            15
                                            9.81                                          50             43.24
                                                                                                                                              Triton [30]. Specifically, we set a maximum batch size 𝐵 as
                            10
                                   7.00
                            5                                                             25                                                  large as possible for each experiment, according to the GPU
                                                                                                7.00
                            0
                                    Orca    Orca    Orca     vLLM
                                                                                           0
                                                                                                 Orca     Orca    Orca     vLLM
                                                                                                                                              memory capacity. The scheduler takes up to 𝐵 number of
                                   (Max)   (Pow2) (Oracle)                                      (Max)    (Pow2) (Oracle)                      earliest arrived requests and sends the batch to FasterTrans-
                                       (a) ShareGPT                                                 (b) Alpaca                                former for processing.
Figure 13. Average number of batched requests when serv-                                                                                      Baseline 2: Orca. Orca [60] is a state-of-the-art LLM serving
ing OPT-13B for the ShareGPT (2 reqs/s) and Alpaca (30                                                                                        system optimized for throughput. Since Orca is not publicly
reqs/s) traces.                                                                                                                               available for use, we implement our own version of Orca. We
6.1                              Experimental Setup                                                                                           assume Orca uses the buddy allocation algorithm to deter-
                                                                                                                                              mine the memory address to store KV cache. We implement
Model and server configurations. We use OPT [62] mod-                                                                                         three versions of Orca based on how much it over-reserves
els with 13B, 66B, and 175B parameters and LLaMA [52] with                                                                                    the space for request outputs:
13B parameters for our evaluation. 13B and 66B are popular                                                                                    • Orca (Oracle). We assume the system has the knowledge
sizes for LLMs as shown in an LLM leaderboard [38], while                                                                                       of the lengths of the outputs that will be actually generated
175B is the size of the famous GPT-3 [5] model. For all of                                                                                      for the requests. This shows the upper-bound performance
our experiments, we use A2 instances with NVIDIA A100                                                                                           of Orca, which is infeasible to achieve in practice.
GPUs on Google Cloud Platform. The detailed model sizes                                                                                       • Orca (Pow2). We assume the system over-reserves the
and server configurations are shown in Table 1.                                                                                                 space for outputs by at most 2×. For example, if the true
                                                                                                                                                output length is 25, it reserves 32 positions for outputs.
Workloads. We synthesize workloads based on ShareGPT [51]
                                                                                                                                              • Orca (Max). We assume the system always reserves the
and Alpaca [50] datasets, which contain input and output
                                                                                                                                                space up to the maximum sequence length of the model,
texts of real LLM services. The ShareGPT dataset is a collec-
                                                                                                                                                i.e., 2048 tokens.
tion of user-shared conversations with ChatGPT [35]. The
Alpaca dataset is an instruction dataset generated by GPT-                                                                                    Key metrics. We focus on serving throughput. Specifically,
3.5 with self-instruct [57]. We tokenize the datasets and use                                                                                 using the workloads with different request rates, we mea-
their input and output lengths to synthesize client requests.                                                                                 sure normalized latency of the systems, the mean of every
As shown in Fig. 11, the ShareGPT dataset has 8.4× longer                                                                                     request’s end-to-end latency divided by its output length,
input prompts and 5.8× longer outputs on average than the                                                                                     as in Orca [60]. A high-throughput serving system should
Alpaca dataset, with higher variance. Since these datasets do                                                                                 retain low normalized latency against high request rates.
not include timestamps, we generate request arrival times                                                                                     For most experiments, we evaluate the systems with 1-hour
using Poisson distribution with different request rates.                                                                                      traces. As an exception, we use 15-minute traces for the
                                                                                                                                              OPT-175B model due to the cost limit.
Baseline 1: FasterTransformer. FasterTransformer [31] is
a distributed inference engine highly optimized for latency.
                                                                                                                                         10
                                                             Orca (Max)               Orca (Pow2)                                Orca (Oracle)                   vLLM
Normalized latency



                     1.0                                                 1.0                                                                          1.0
   (s/token)




                     0.5                                                 0.5                                                                          0.5

                     0.0                                                 0.0                                                                          0.0
                           0         5       10         15                     0      2       4     6       8                            10                  0                       2        4           6
                                     Request rate (req/s)                                  Request rate (req/s)                                                                      Request rate (req/s)

                           (a) parallel generation (parallel size = 2)         (b) parallel generation (parallel size = 4)                                   (c) parallel generation (parallel size = 6)
Normalized latency




                     1.0                                                 1.0                                                                          1.0
   (s/token)




                     0.5                                                 0.5                                                                          0.5

                     0.0                                                 0.0                                                                          0.0
                           0         5        10          15                   0       2       4       6       8                              10             0                       2        4           6
                                     Request rate (req/s)                                  Request rate (req/s)                                                                      Request rate (req/s)

                               (d) beam search (beam width = 2)                    (e) beam search (beam width = 4)                                              (f) beam search (beam width = 6)


                                        Figure 14. Parallel generation and beam search with OPT-13B on the Alpaca dataset.




                                                                                                                                                                      Memory saving (%)
                                                                                                                          12
6.2                  Basic Sampling

                                                                                                      Memory saving (%)
                                                                                                                                                       9.79                               60             53.13      55.16
                                                                                                                                              8.53
                                                                                                                           8                                                                   37.56
                                                                                                                                 6.09                                                     40

We evaluate the performance of vLLM with basic sampling                                                                    4                                                              20
(one sample per request) on three models and two datasets.                                                                 0                                                               0
                                                                                                                                  2            4         6                                      2          4         6
The first row of Fig. 12 shows the results on the ShareGPT                                                                            # Output sequences                                               Beam width

dataset. The curves illustrate that as the request rate in-                                                                    (a) Parallel sampling                                           (b) Beam search
creases, the latency initially increases at a gradual pace but
then suddenly explodes. This can be attributed to the fact                                          Figure 15. Average amount of memory saving from sharing
that when the request rate surpasses the capacity of the serv-                                      KV blocks, when serving OPT-13B for the Alpaca trace.
ing system, the queue length continues to grow infinitely
and so does the latency of the requests.                                                            6.3                        Parallel Sampling and Beam Search
   On the ShareGPT dataset, vLLM can sustain 1.7×–2.7×                                              We evaluate the effectiveness of memory sharing in Page-
higher request rates compared to Orca (Oracle) and 2.7×–8×                                          dAttention with two popular sampling methods: parallel
compared to Orca (Max), while maintaining similar laten-                                            sampling and beam search. In parallel sampling, all paral-
cies. This is because vLLM’s PagedAttention can efficiently                                         lel sequences in a request can share the KV cache for the
manage the memory usage and thus enable batching more                                               prompt. As shown in the first row of Fig. 14, with a larger
requests than Orca. For example, as shown in Fig. 13a, for                                          number of sequences to sample, vLLM brings more improve-
OPT-13B vLLM processes 2.2× more requests at the same                                               ment over the Orca baselines. Similarly, the second row of
time than Orca (Oracle) and 4.3× more requests than Orca                                            Fig. 14 shows the results for beam search with different beam
(Max). Compared to FasterTransformer, vLLM can sustain up                                           widths. Since beam search allows for more sharing, vLLM
to 22× higher request rates, as FasterTransformer does not                                          demonstrates even greater performance benefits. The im-
utilize a fine-grained scheduling mechanism and inefficiently                                       provement of vLLM over Orca (Oracle) on OPT-13B and the
manages the memory like Orca (Max).                                                                 Alpaca dataset goes from 1.3× in basic sampling to 2.3× in
   The second row of Fig. 12 and Fig. 13b shows the results                                         beam search with a width of 6.
on the Alpaca dataset, which follows a similar trend to the                                            Fig. 15 plots the amount of memory saving, computed by
ShareGPT dataset. One exception is Fig. 12 (f), where vLLM’s                                        the number of blocks we saved by sharing divided by the
advantage over Orca (Oracle) and Orca (Pow2) is less pro-                                           number of total blocks without sharing. We show 6.1% - 9.8%
nounced. This is because the model and server configuration                                         memory saving on parallel sampling and 37.6% - 55.2% on
for OPT-175B (Table 1) allows for large GPU memory space                                            beam search. In the same experiments with the ShareGPT
available to store KV cache, while the Alpaca dataset has                                           dataset, we saw 16.2% - 30.5% memory saving on parallel
short sequences. In this setup, Orca (Oracle) and Orca (Pow2)                                       sampling and 44.3% - 66.3% on beam search.
can also batch a large number of requests despite the inef-
ficiencies in their memory management. As a result, the                                             6.4                        Shared prefix
performance of the systems becomes compute-bound rather                                             We explore the effectiveness of vLLM for the case a prefix
than memory-bound.                                                                                  is shared among different input prompts, as illustrated in
                                                                                               11
                                                           Orca (Oracle)                     vLLM                                                    vLLM (bs 8)      vLLM (bs 32)




                                                                                                                                                                                     Normalized latency (s/token)
                                                                                                                                                     FT (bs 8)        FT (bs 32)                                                   ShareGPT
      Normalized latency

                                                                                                                                                                                                                    17.5
                                                                                                                                          250
                               1.0                                       1.0                                                                                                                                                       Alpaca




                                                                                                                    Kernel latency (us)
                                                                                                                                                                                                                    15.0
                                                                                                                                          200
                                                                                                                                                                                                                    12.5

                                                                                                                                          150
         (s/token)



                                                                                                                                                                                                                    10.0

                                                                                                                                                                                                                     7.5
                               0.5                                       0.5                                                              100
                                                                                                                                                                                                                     5.0
                                                                                                                                           50                                                                        2.5

                                                                                                                                            0                                                                        0.0
                                                                                                                                                64        128               256                                            1   2     4   8    16   32   64 128 256
                               0.0                                       0.0                                                                              Context length                                                                 Block size
                                         0       20       40                   0         20        40
                                             Request rate (req/s)                  Request rate (req/s)         (a) Latency of attention kernels. (b) End-to-end latency with dif-
                                        (a) 1-shot prefix prompt           (b) 5-shot prefix prompt                                               ferent block sizes.
                                                                                                                                                            Figure 18. Ablation experiments.
Figure 16. Translation workload where the input prompts
share a common prefix. The prefix includes (a) 1 example
with 80 tokens or (b) 5 examples with 341 tokens.
                                                                                                                handle the long prompts, as PagedAttention resolves the
                                        Orca (Max)         Orca (Pow2)         Orca (Oracle)        vLLM        problem of memory fragmentation and reservation.
                                        1.0
                   Normalized latency




                                                                                                                7                          Ablation Studies
                      (s/token)




                                        0.5
                                                                                                                In this section, we study various aspects of vLLM and evalu-
                                        0.0
                                                                                                                ate the design choices we make with ablation experiments.
                                           0.0       0.2       0.4        0.6          0.8
                                                           Request rate (req/s)
                                                                                                                7.1                             Kernel Microbenchmark
                    Figure 17. Performance on chatbot workload.                                                 The dynamic block mapping in PagedAttention affects the
                                                                                                                performance of the GPU operations involving the stored KV
Fig. 10. For the model, we use LLaMA-13B [52], which is mul-                                                    cache, i.e., block read/writes and attention. Compared to the
tilingual. For the workload, we use the WMT16 [4] English-                                                      existing systems, our GPU kernels (§5) involve extra over-
to-German translation dataset and synthesize two prefixes                                                       heads of accessing the block table, executing extra branches,
that include an instruction and a few translation examples.                                                     and handling variable sequence lengths. As shown in Fig. 18a,
The first prefix includes a single example (i.e., one-shot)                                                     this leads to 20–26% higher attention kernel latency, com-
while the other prefix includes 5 examples (i.e., few-shot). As                                                 pared to the highly-optimized FasterTransformer implemen-
shown in Fig. 16 (a), vLLM achieves 1.67× higher through-                                                       tation. We believe the overhead is small as it only affects
put than Orca (Oracle) when the one-shot prefix is shared.                                                      the attention operator but not the other operators in the
Furthermore, when more examples are shared (Fig. 16 (b)),                                                       model, such as Linear. Despite the overhead, PagedAttention
vLLM achieves 3.58× higher throughput than Orca (Oracle).                                                       makes vLLM significantly outperform FasterTransformer in
                                                                                                                end-to-end performance (§6).
6.5             Chatbot
                                                                                                                7.2                             Impact of Block Size
A chatbot [8, 19, 35] is one of the most important applications
of LLMs. To implement a chatbot, we let the model generate                                                      The choice of block size can have a substantial impact on the
a response by concatenating the chatting history and the                                                        performance of vLLM. If the block size is too small, vLLM
last user query into a prompt. We synthesize the chatting                                                       may not fully utilize the GPU’s parallelism for reading and
history and user query using the ShareGPT dataset. Due to                                                       processing KV cache. If the block size is too large, inter-
the limited context length of the OPT-13B model, we cut the                                                     nal fragmentation increases and the probability of sharing
prompt to the last 1024 tokens and let the model generate                                                       decreases.
at most 1024 tokens. We do not store the KV cache between                                                          In Fig. 18b, we evaluate the performance of vLLM with dif-
different conversation rounds as doing this would occupy the                                                    ferent block sizes, using the ShareGPT and Alpaca traces with
space for other requests between the conversation rounds.                                                       basic sampling under fixed request rates. In the ShareGPT
   Fig. 17 shows that vLLM can sustain 2× higher request                                                        trace, block sizes from 16 to 128 lead to the best performance.
rates compared to the three Orca baselines. Since the ShareGPT                                                  In the Alpaca trace, while the block size 16 and 32 work
dataset contains many long conversations, the input prompts                                                     well, larger block sizes significantly degrade the performance
for most requests have 1024 tokens. Due to the buddy allo-                                                      since the sequences become shorter than the block sizes. In
cation algorithm, the Orca baselines reserve the space for                                                      practice, we find that the block size 16 is large enough to
1024 tokens for the request outputs, regardless of how they                                                     efficiently utilize the GPU and small enough to avoid signifi-
predict the output lengths. For this reason, the three Orca                                                     cant internal fragmentation in most workloads. Accordingly,
baselines behave similarly. In contrast, vLLM can effectively                                                   vLLM sets its default block size as 16.
                                                                                                           12
                                                             Normalized latency (s/token)
                140                        Recompute                                        2.5                             Recompute           swap-out policy, which exploits the fact that processing a
                120                        Swap in                                                                          Swap

                100
                                           Swap out
                                                                                            2.0                                                 request requires all of its corresponding token states to be
    Time (ms)




                                           Swap in + out
                80
                                                                                            1.5
                                                                                                                                                stored in GPU memory. Another example is the recomputa-
                60

                40
                                                                                            1.0
                                                                                                                                                tion method to recover the evicted blocks, which is not feasi-
                                                                                            0.5
                20                                                                                                                              ble in OS. Besides, vLLM mitigates the overhead of memory
                 0                                                                          0.0
                      1   2   4   8   16   32
                                  Block size
                                                64 128 256                                        1   2   4   8   16   32   64   128 256        indirection in paging by fusing the GPU kernels for memory
                                                                                                              Block size

                  (a) Microbenchmark                         (b) End-to-end performance                                                         access operations with those for other operations such as
                                                                                                                                                attention.
Figure 19. (a) Overhead of recomputation and swapping for
different block sizes. (b) Performance when serving OPT-13B                                                                                     9   Related Work
with the ShareGPT traces at the same request rate.
                                                                                                                                                General model serving systems. Model serving has been
7.3               Comparing Recomputation and Swapping                                                                                          an active area of research in recent years, with numerous
                                                                                                                                                systems proposed to tackle diverse aspects of deep learning
vLLM supports both recomputation and swapping as its re-
                                                                                                                                                model deployment. Clipper [11], TensorFlow Serving [33],
covery mechanisms. To understand the tradeoffs between
                                                                                                                                                Nexus [45], InferLine [10], and Clockwork [20] are some
the two methods, we evaluate their end-to-end performance
                                                                                                                                                earlier general model serving systems. They study batch-
and microbenchmark their overheads, as presented in Fig. 19.
                                                                                                                                                ing, caching, placement, and scheduling for serving single
Our results reveal that swapping incurs excessive overhead
                                                                                                                                                or multiple models. More recently, DVABatch [12] intro-
with small block sizes. This is because small block sizes often
                                                                                                                                                duces multi-entry multi-exit batching. REEF [21] and Shep-
result in numerous small data transfers between CPU and
                                                                                                                                                herd [61] propose preemption for serving. AlpaServe [28]
GPU, which limits the effective PCIe bandwidth. In contrast,
                                                                                                                                                utilizes model parallelism for statistical multiplexing. How-
the overhead of recomputation remains constant across dif-
                                                                                                                                                ever, these general systems fail to take into account the auto-
ferent block sizes, as recomputation does not utilize the KV
                                                                                                                                                regressive property and token state of LLM inference, result-
blocks. Thus, recomputation is more efficient when the block
                                                                                                                                                ing in missed opportunities for optimization.
size is small, while swapping is more efficient when the block
size is large, though recomputation overhead is never higher                                                                                    Specialized serving systems for transformers. Due to
than 20% of swapping’s latency. For medium block sizes from                                                                                     the significance of the transformer architecture, numerous
16 to 64, the two methods exhibit comparable end-to-end                                                                                         specialized serving systems for it have been developed. These
performance.                                                                                                                                    systems utilize GPU kernel optimizations [1, 29, 31, 56], ad-
                                                                                                                                                vanced batching mechanisms [14, 60], model parallelism [1,
8               Discussion                                                                                                                      41, 60], and parameter sharing [64] for efficient serving.
Applying the virtual memory and paging technique to                                                                                             Among them, Orca [60] is most relevant to our approach.
other GPU workloads. The idea of virtual memory and                                                                                             Comparison to Orca. The iteration-level scheduling in
paging is effective for managing the KV cache in LLM serving                                                                                    Orca [60] and PagedAttention in vLLM are complementary
because the workload requires dynamic memory allocation                                                                                         techniques: While both systems aim to increase the GPU
(since the output length is not known a priori) and its perfor-                                                                                 utilization and hence the throughput of LLM serving, Orca
mance is bound by the GPU memory capacity. However, this                                                                                        achieves it by scheduling and interleaving the requests so
does not generally hold for every GPU workload. For exam-                                                                                       that more requests can be processed in parallel, while vLLM
ple, in DNN training, the tensor shapes are typically static,                                                                                   is doing so by increasing memory utilization so that the
and thus memory allocation can be optimized ahead of time.                                                                                      working sets of more requests fit into memory. By reducing
For another example, in serving DNNs that are not LLMs,                                                                                         memory fragmentation and enabling sharing, vLLM runs
an increase in memory efficiency may not result in any per-                                                                                     more requests in a batch in parallel and achieves a 2-4×
formance improvement since the performance is primarily                                                                                         speedup compared to Orca. Indeed, the fine-grained sched-
compute-bound. In such scenarios, introducing the vLLM’s                                                                                        uling and interleaving of the requests like in Orca makes
techniques may rather degrade the performance due to the                                                                                        memory management more challenging, making the tech-
extra overhead of memory indirection and non-contiguous                                                                                         niques proposed in vLLM even more crucial.
block memory. However, we would be excited to see vLLM’s                                                                                        Memory optimizations. The widening gap between the
techniques being applied to other workloads with similar                                                                                        compute capability and memory capacity of accelerators has
properties to LLM serving.                                                                                                                      caused memory to become a bottleneck for both training
LLM-specific optimizations in applying virtual mem-                                                                                             and inference. Swapping [23, 42, 55], recomputation [7, 24]
ory and paging. vLLM re-interprets and augments the idea                                                                                        and their combination [40] have been utilized to reduce the
of virtual memory and paging by leveraging the application-                                                                                     peak memory of training. Notably, FlexGen [46] studies how
specific semantics. One example is vLLM’s all-or-nothing                                                                                        to swap weights and token states for LLM inference with
                                                                                                                                           13
limited GPU memory, but it does not target the online serv-                             Joseph, Greg Brockman, et al. 2021. Evaluating large language models
ing settings. OLLA [48] optimizes the lifetime and location                             trained on code. arXiv preprint arXiv:2107.03374 (2021).
of tensors to reduce fragmentation, but it does not do fine-                        [7] Tianqi Chen, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. 2016.
                                                                                        Training deep nets with sublinear memory cost. arXiv preprint
grained block-level management or online serving. FlashAt-                              arXiv:1604.06174 (2016).
tention [13] applies tiling and kernel optimizations to reduce                      [8] Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng, Zhanghao Wu, Hao
the peak memory of attention computation and reduce I/O                                 Zhang, Lianmin Zheng, Siyuan Zhuang, Yonghao Zhuang, Joseph E.
costs. This paper introduces a new idea of block-level mem-                             Gonzalez, Ion Stoica, and Eric P. Xing. 2023. Vicuna: An Open-Source
ory management in the context of online serving.                                        Chatbot Impressing GPT-4 with 90%* ChatGPT Quality. https://lmsys.
                                                                                        org/blog/2023-03-30-vicuna/
10    Conclusion                                                                    [9] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma,
                                                                                        Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung,
This paper proposes PagedAttention, a new attention algo-                               Charles Sutton, Sebastian Gehrmann, et al. 2022. Palm: Scaling lan-
rithm that allows attention keys and values to be stored                                guage modeling with pathways. arXiv preprint arXiv:2204.02311 (2022).
                                                                                   [10] Daniel Crankshaw, Gur-Eyal Sela, Xiangxi Mo, Corey Zumar, Ion
in non-contiguous paged memory, and presents vLLM, a                                    Stoica, Joseph Gonzalez, and Alexey Tumanov. 2020. InferLine: latency-
high-throughput LLM serving system with efficient mem-                                  aware provisioning and scaling for prediction serving pipelines. In
ory management enabled by PagedAttention. Inspired by                                   Proceedings of the 11th ACM Symposium on Cloud Computing. 477–491.
operating systems, we demonstrate how established tech-                            [11] Daniel Crankshaw, Xin Wang, Guilio Zhou, Michael J Franklin,
niques, such as virtual memory and copy-on-write, can be                                Joseph E Gonzalez, and Ion Stoica. 2017. Clipper: A Low-Latency
                                                                                        Online Prediction Serving System. In 14th USENIX Symposium on
adapted to efficiently manage KV cache and handle various                               Networked Systems Design and Implementation (NSDI 17). 613–627.
decoding algorithms in LLM serving. Our experiments show                           [12] Weihao Cui, Han Zhao, Quan Chen, Hao Wei, Zirui Li, Deze Zeng,
that vLLM achieves 2-4× throughput improvements over the                                Chao Li, and Minyi Guo. 2022. DVABatch: Diversity-aware Multi-
state-of-the-art systems.                                                               Entry Multi-Exit Batching for Efficient Processing of DNN Services
                                                                                        on GPUs. In 2022 USENIX Annual Technical Conference (USENIX ATC
Acknowledgement                                                                         22). 183–198.
                                                                                   [13] Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and Christopher Ré.
We would like to thank Xiaoxuan Liu, Zhifeng Chen, Yan-                                 2022. Flashattention: Fast and memory-efficient exact attention with
ping Huang, anonymous SOSP reviewers, and our shepherd,                                 io-awareness. Advances in Neural Information Processing Systems 35
Lidong Zhou, for their insightful feedback. This research is                            (2022), 16344–16359.
                                                                                   [14] Jiarui Fang, Yang Yu, Chengduo Zhao, and Jie Zhou. 2021. TurboTrans-
partly supported by gifts from Andreessen Horowitz, Anyscale,
                                                                                        formers: an efficient GPU serving system for transformer models. In
Astronomer, Google, IBM, Intel, Lacework, Microsoft, Mo-                                Proceedings of the 26th ACM SIGPLAN Symposium on Principles and
hamed Bin Zayed University of Artificial Intelligence, Sam-                             Practice of Parallel Programming. 389–402.
sung SDS, Uber, and VMware.                                                        [15] FastAPI. 2023. FastAPI. https://github.com/tiangolo/fastapi.
                                                                                   [16] Pin Gao, Lingfan Yu, Yongwei Wu, and Jinyang Li. 2018. Low latency
References                                                                              rnn inference with cellular batching. In Proceedings of the Thirteenth
                                                                                        EuroSys Conference. 1–15.
 [1] Reza Yazdani Aminabadi, Samyam Rajbhandari, Minjia Zhang, Am-                 [17] Amir Gholami, Zhewei Yao, Sehoon Kim, Michael W Mahoney, and
     mar Ahmad Awan, Cheng Li, Du Li, Elton Zheng, Jeff Rasley, Shaden                  Kurt Keutzer. 2021. Ai and memory wall. RiseLab Medium Post 1 (2021),
     Smith, Olatunji Ruwase, et al. 2022. DeepSpeed Inference: Enabling                 6.
     Efficient Inference of Transformer Models at Unprecedented Scale.
                                                                                   [18] Github. 2022. https://github.com/features/copilot
     arXiv preprint arXiv:2207.00032 (2022).                                       [19] Google. 2023. https://bard.google.com/
 [2] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. 2016. Layer            [20] Arpan Gujarati, Reza Karimi, Safya Alzayat, Wei Hao, Antoine Kauf-
     normalization. arXiv preprint arXiv:1607.06450 (2016).                             mann, Ymir Vigfusson, and Jonathan Mace. 2020. Serving {DNNs} like
 [3] Yoshua Bengio, Réjean Ducharme, and Pascal Vincent. 2000. A neural                 Clockwork: Performance Predictability from the Bottom Up. In 14th
     probabilistic language model. Advances in neural information process-              USENIX Symposium on Operating Systems Design and Implementation
     ing systems 13 (2000).                                                             (OSDI 20). 443–462.
 [4] Ond rej Bojar, Rajen Chatterjee, Christian Federmann, Yvette Gra-             [21] Mingcong Han, Hanze Zhang, Rong Chen, and Haibo Chen.
     ham, Barry Haddow, Matthias Huck, Antonio Jimeno Yepes, Philipp                    2022.      Microsecond-scale Preemption for Concurrent {GPU-
     Koehn, Varvara Logacheva, Christof Monz, Matteo Negri, Aurelie                     accelerated} {DNN} Inferences. In 16th USENIX Symposium on Oper-
     Neveol, Mariana Neves, Martin Popel, Matt Post, Raphael Rubino, Car-               ating Systems Design and Implementation (OSDI 22). 539–558.
     olina Scarton, Lucia Specia, Marco Turchi, Karin Verspoor, and Marcos         [22] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep
     Zampieri. 2016. Findings of the 2016 Conference on Machine Trans-                  residual learning for image recognition. In Proceedings of the IEEE
     lation. In Proceedings of the First Conference on Machine Translation.             conference on computer vision and pattern recognition. 770–778.
     Association for Computational Linguistics, Berlin, Germany, 131–198.
                                                                                   [23] Chien-Chin Huang, Gu Jin, and Jinyang Li. 2020. Swapadvisor: Push-
     http://www.aclweb.org/anthology/W/W16/W16-2301                                     ing deep learning beyond the gpu memory limit via smart swapping.
 [5] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D                     In Proceedings of the Twenty-Fifth International Conference on Archi-
     Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish                tectural Support for Programming Languages and Operating Systems.
     Sastry, Amanda Askell, et al. 2020. Language models are few-shot                   1341–1355.
     learners. Advances in neural information processing systems 33 (2020),        [24] Paras Jain, Ajay Jain, Aniruddha Nrusimha, Amir Gholami, Pieter
     1877–1901.                                                                         Abbeel, Joseph Gonzalez, Kurt Keutzer, and Ion Stoica. 2020. Check-
 [6] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde                   mate: Breaking the memory wall with optimal tensor rematerialization.
     de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas
                                                                              14
     Proceedings of Machine Learning and Systems 2 (2020), 497–511.                       Language Models with a Single GPU. arXiv preprint arXiv:2303.06865
[25] Tom Kilburn, David BG Edwards, Michael J Lanigan, and Frank H                        (2023).
     Sumner. 1962. One-level storage system. IRE Transactions on Electronic          [47] Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley,
     Computers 2 (1962), 223–235.                                                         Jared Casper, and Bryan Catanzaro. 2019. Megatron-lm: Training multi-
[26] Brian Lester, Rami Al-Rfou, and Noah Constant. 2021. The power                       billion parameter language models using model parallelism. arXiv
     of scale for parameter-efficient prompt tuning. arXiv preprint                       preprint arXiv:1909.08053 (2019).
     arXiv:2104.08691 (2021).                                                        [48] Benoit Steiner, Mostafa Elhoushi, Jacob Kahn, and James Hegarty. 2022.
[27] Xiang Lisa Li and Percy Liang. 2021. Prefix-tuning: Optimizing contin-               OLLA: Optimizing the Lifetime and Location of Arrays to Reduce the
     uous prompts for generation. arXiv preprint arXiv:2101.00190 (2021).                 Memory Usage of Neural Networks. (2022). https://doi.org/10.48550/
[28] Zhuohan Li, Lianmin Zheng, Yinmin Zhong, Vincent Liu, Ying Sheng,                    arXiv.2210.12924
     Xin Jin, Yanping Huang, Zhifeng Chen, Hao Zhang, Joseph E Gonzalez,             [49] Ilya Sutskever, Oriol Vinyals, and Quoc V Le. 2014. Sequence to se-
     et al. 2023. AlpaServe: Statistical Multiplexing with Model Parallelism              quence learning with neural networks. Advances in neural information
     for Deep Learning Serving. arXiv preprint arXiv:2302.11665 (2023).                   processing systems 27 (2014).
[29] Lingxiao Ma, Zhiqiang Xie, Zhi Yang, Jilong Xue, Youshan Miao, Wei              [50] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen
     Cui, Wenxiang Hu, Fan Yang, Lintao Zhang, and Lidong Zhou. 2020.                     Li, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. 2023.
     Rammer: Enabling holistic deep learning compiler optimizations with                  Stanford Alpaca: An Instruction-following LLaMA model. https://
     rtasks. In Proceedings of the 14th USENIX Conference on Operating                    github.com/tatsu-lab/stanford_alpaca.
     Systems Design and Implementation. 881–897.                                     [51] ShareGPT Team. 2023. https://sharegpt.com/
[30] NVIDIA. [n. d.]. Triton Inference Server. https://developer.nvidia.com/         [52] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-
     nvidia-triton-inference-server.                                                      Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric
[31] NVIDIA. 2023. FasterTransformer. https://github.com/NVIDIA/                          Hambro, Faisal Azhar, et al. 2023. Llama: Open and efficient foundation
     FasterTransformer.                                                                   language models. arXiv preprint arXiv:2302.13971 (2023).
[32] NVIDIA. 2023. NCCL: The NVIDIA Collective Communication Library.                [53] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion
     https://developer.nvidia.com/nccl.                                                   Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. At-
[33] Christopher Olston, Noah Fiedel, Kiril Gorovoy, Jeremiah Harmsen, Li                 tention is all you need. Advances in neural information processing
     Lao, Fangwei Li, Vinu Rajashekhar, Sukriti Ramesh, and Jordan Soyke.                 systems 30 (2017).
     2017. Tensorflow-serving: Flexible, high-performance ml serving.                [54] Jing Wang, Youyou Lu, Qing Wang, Minhui Xie, Keji Huang, and Jiwu
     arXiv preprint arXiv:1712.06139 (2017).                                              Shu. 2022. Pacman: An Efficient Compaction Approach for {Log-
[34] OpenAI. 2020. https://openai.com/blog/openai-api                                     Structured} {Key-Value} Store on Persistent Memory. In 2022 USENIX
[35] OpenAI. 2022. https://openai.com/blog/chatgpt                                        Annual Technical Conference (USENIX ATC 22). 773–788.
[36] OpenAI. 2023. https://openai.com/blog/custom-instructions-for-                  [55] Linnan Wang, Jinmian Ye, Yiyang Zhao, Wei Wu, Ang Li, Shuai-
     chatgpt                                                                              wen Leon Song, Zenglin Xu, and Tim Kraska. 2018. Superneurons: Dy-
[37] OpenAI. 2023. GPT-4 Technical Report. arXiv:2303.08774 [cs.CL]                       namic GPU memory management for training deep neural networks.
[38] LMSYS ORG. 2023. Chatbot Arena Leaderboard Week 8: Introduc-                         In Proceedings of the 23rd ACM SIGPLAN symposium on principles and
     ing MT-Bench and Vicuna-33B. https://lmsys.org/blog/2023-06-22-                      practice of parallel programming. 41–53.
     leaderboard/.                                                                   [56] Xiaohui Wang, Ying Xiong, Yang Wei, Mingxuan Wang, and Lei Li.
[39] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James                           2021. LightSeq: A High Performance Inference Library for Transform-
     Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia                        ers. In Proceedings of the 2021 Conference of the North American Chapter
     Gimelshein, Luca Antiga, et al. 2019. Pytorch: An imperative style,                  of the Association for Computational Linguistics: Human Language Tech-
     high-performance deep learning library. Advances in neural informa-                  nologies: Industry Papers. 113–120.
     tion processing systems 32 (2019).                                              [57] Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A
[40] Shishir G Patil, Paras Jain, Prabal Dutta, Ion Stoica, and Joseph Gon-               Smith, Daniel Khashabi, and Hannaneh Hajishirzi. 2022. Self-Instruct:
     zalez. 2022. POET: Training Neural Networks on Tiny Devices with                     Aligning Language Model with Self Generated Instructions. arXiv
     Integrated Rematerialization and Paging. In International Conference                 preprint arXiv:2212.10560 (2022).
     on Machine Learning. PMLR, 17573–17583.                                         [58] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond,
[41] Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin,                      Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf,
     James Bradbury, Anselm Levskaya, Jonathan Heek, Kefan Xiao, Shivani                  Morgan Funtowicz, et al. 2020. Transformers: State-of-the-art natural
     Agrawal, and Jeff Dean. 2022. Efficiently Scaling Transformer Inference.             language processing. In Proceedings of the 2020 conference on empirical
     arXiv preprint arXiv:2211.05102 (2022).                                              methods in natural language processing: system demonstrations. 38–45.
[42] Jie Ren, Samyam Rajbhandari, Reza Yazdani Aminabadi, Olatunji                   [59] Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le, Mohammad
     Ruwase, Shuangyan Yang, Minjia Zhang, Dong Li, and Yuxiong He.                       Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao,
     2021. ZeRO-Offload: Democratizing Billion-Scale Model Training.. In                  Klaus Macherey, et al. 2016. Google’s neural machine translation
     USENIX Annual Technical Conference. 551–564.                                         system: Bridging the gap between human and machine translation.
[43] Reuters. 2023. https://www.reuters.com/technology/tech-giants-ai-                    arXiv preprint arXiv:1609.08144 (2016).
     like-bing-bard-poses-billion-dollar-search-problem-2023-02-22/                  [60] Gyeong-In Yu, Joo Seong Jeong, Geon-Woo Kim, Soojeong Kim, and
[44] Amazon Web Services. 2023. https://aws.amazon.com/bedrock/                           Byung-Gon Chun. 2022. Orca: A Distributed Serving System for
[45] Haichen Shen, Lequn Chen, Yuchen Jin, Liangyu Zhao, Bingyu Kong,                     {Transformer-Based} Generative Models. In 16th USENIX Symposium
     Matthai Philipose, Arvind Krishnamurthy, and Ravi Sundaram. 2019.                    on Operating Systems Design and Implementation (OSDI 22). 521–538.
     Nexus: A GPU cluster engine for accelerating DNN-based video anal-              [61] Hong Zhang, Yupeng Tang, Anurag Khandelwal, and Ion Stoica. 2023.
     ysis. In Proceedings of the 27th ACM Symposium on Operating Systems                  SHEPHERD: Serving DNNs in the Wild. In 20th USENIX Symposium on
     Principles. 322–337.                                                                 Networked Systems Design and Implementation (NSDI 23). USENIX As-
[46] Ying Sheng, Lianmin Zheng, Binhang Yuan, Zhuohan Li, Max Ryabinin,                   sociation, Boston, MA, 787–808. https://www.usenix.org/conference/
     Daniel Y Fu, Zhiqiang Xie, Beidi Chen, Clark Barrett, Joseph E Gon-                  nsdi23/presentation/zhang-hong
     zalez, et al. 2023. High-throughput Generative Inference of Large

                                                                                15
[62] Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen,              Eric P Xing, et al. 2022. Alpa: Automating Inter-and Intra-Operator
     Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria                 Parallelism for Distributed Deep Learning. In 16th USENIX Symposium
     Lin, et al. 2022. Opt: Open pre-trained transformer language models.             on Operating Systems Design and Implementation (OSDI 22). 559–578.
     arXiv preprint arXiv:2205.01068 (2022).                                     [64] Zhe Zhou, Xuechao Wei, Jiejing Zhang, and Guangyu Sun. 2022. PetS:
[63] Lianmin Zheng, Zhuohan Li, Hao Zhang, Yonghao Zhuang, Zhifeng                    A Unified Framework for Parameter-Efficient Transformers Serving. In
     Chen, Yanping Huang, Yida Wang, Yuanzhong Xu, Danyang Zhuo,                      2022 USENIX Annual Technical Conference (USENIX ATC 22). 489–504.




                                                                            16
```
