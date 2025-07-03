
*********************INFORMATION*****************************

TAP-DLND 1.0 : A Corpus For Document Level Novelty Detection

Authors : Tirthankar Ghosal, Amitra Salam, Swati Tiwari, Asif Ekbal and Pushpak Bhattacharyya

Affiliation : Indian Institute of Technology Patna, India

Corresponding Author : Tirthankar Ghosal (tirthankar.slg@gmail.com)

Updated as on : 22nd February, 2018

********************PUBLICATION*******************************

This work has been accepted for publication and oral presentation in Language Resources and Evaluation Conference (LREC) 2018 to be held at Miyazaki, Japan from May 7th-12th, 2018. The dataset TAP-DLND 1.0 shall also be available via European Language Resource Association (ELRA). One may contact the first author for the dataset for research purpose only. The dataset would also be hosted in institution repository. http://www.iitp.ac.in/ai-nlp-ml/resources.html.

*******************ACKNOWLEDGEMENT***************************

TAP-DLND 1.0 : Tirthankar-Asif-Pushpak Document Level Novelty Detection version 1.0 (after the names of the principal investigators). The first author is supported by Visvesvaraya PhD Scheme, Ministry of Electronics and Information Technology (MeitY), Government of India implemented by Digital India Corporation (formerly Media Lab Asia). The fourth author is the recipient of Sir Visvesvaraya Young Faculty Research Fellow Award, Ministry of Electronics and Information Technology (MeitY), Government of India. The work is generously supported by Elsevier Centre of Excellence for Natural Language Processing, Department of Computer Science and Engineering, Indian Institute of Technology Patna.

*********************REFERENCE********************************

Pre-print Bibtex for the paper :

@article{ghosal2018tap,
  title={TAP-DLND 1.0: A Corpus for Document Level Novelty Detection},
  author={Ghosal, Tirthankar and Salam, Amitra and Tiwari, Swati and Ekbal, Asif and Bhattacharyya, Pushpak},
  journal={arXiv preprint arXiv:1802.06950},
  year={2018}
}

********************DESCRIPTION*******************************

1.	The dataset consists 10 categories of news events in separate folders.

ACCIDENT			(ACC)
POLITICS			(PLT)
BUSINESS			(BUS)
CRIME				(CRM)
ARTS AND ENTERTAINMENT		(ART)
SPORTS				(SPT)
TERRORISM			(TER)
NATURE				(NAT)
GOVERNMENT			(GOV)
SOCIETY				(SOC)

2.	Each category hosts number of events in separate folders with unique event id's.

3.	Each event consists of news items in folders "source" and "target" from different news agencies.

4.	The "source" folder consists of exactly 3 seed news items in .txt files regarding a particular event. For each news item there is a .xml meta file consisting of information about the news item within structured XML tags.

5.	For each event, the source news items are the ones against which a target news item is judged for "novelty" or "non-novelty".

6.	The "target" folder consists of several news items relevant to the same event. These are the annotated documents. The annotation information is present within the Document Level Annotation (DLA) attribute within the corresponding target meta (.xml) files. Each target document is annotated as "Novel" or "Non-Novel" against the corresponding 3 source items for each event. The ambiguous cases are eliminated from the corpus.

7.	There are 2736 Novel and 2704 Non-Novel target documents.

8.	Each target document is annotated by two annotators. The annotators had post-graduate level knowledge in English. A third annotator resolved the differences via majority voting. The final label is contained within the DLA attribute in the meta file for each target document.

9.	The news items are crawled from various web sources pertaining to each event in a periodic manner.

10.	Each source and target data item is referenced by a unique id.

********************LICENSE***********************************

This work is licensed under a Creative Commons Attribution-NoDerivatives 4.0 International License. 

**************************************************************


