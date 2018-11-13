# About europeana-topics-en-de.tar
This test set was crawled from the [Europeana website](https://www.europeana.eu/portal/en) by manually selecting 100 random pages for four subdomains and extracting about 500 relevant sentences. These sentences were then segmented using the XTM translation management system and stored as plain text files, while removing all mark-up. Translation was carried out using the freely available DeepL4 MT system and post-edited, in order to reduce throughput time and costs. In-house resources (non-native in any of the languages) were used for post-editing. This set-up is similar to the WMT set up, except that our resources have a linguistic background, and pre-translation is used instead of translation from scratch. This effort yielded a test set that is already considerable in size, but probably not sufficiently representative for all data within the Europeana repository. For the time being, it allows us to get an idea of the content and to test our hypotheses about potential MT problems when applying Named Entity Recognition (NER). Test set statistics and example sentences are indicated in the tables below.

# Statistics
| Topic | Language pair | # of sentences | # of tokens |
|-------|---------------|----------------|-------------|
| Art | en-de | 176 | 2.507 |
| Migration | en-de | 191 | 3.649 |
| Music | en-de | 104 | 1.187 |
| Sport | en-de | 47 | 647 |
| Total | | 518 | 7.990 |

# Examples
## Art
| English | German |
|----|----|
|The chintz design consists of a delicate floral meander of stylised pinks and carnations interspersed with a single flower or cluster of flowers tied by a ribbon . | Das Chintz - Design besteht aus einem zarten floralen Mäander aus stilisierten Nelken und Nelken , durchsetzt mit einer einzelnen Blume oder einer Gruppe von Blumen , die durch ein Band gebunden sind . |
| Hand - painted silk tie , designed by Vicky Holton , Great Britain , 1992. | Handbemalte Seidenkrawatte , entworfen von Vicky Holton , Großbritannien , 1992. |
| The central row contains alternately single large wheels , 4.5 inches in diameter , and vertical lines of two half and one whole wheels . | Die mittlere Reihe enthält abwechselnd einzelne große Räder mit einem Durchmesser von 4,5 Zoll und vertikale Linien von zwei halben und einem ganzen Rad . |

## Migration
| English | German |
|----|----|
| Pictured on arrival at London Airport with air hostess Jean Reed they are on their way to Tibetan House in the British Pestalozzi Children ' s Village in Oaklands Park , Sedlescombe , Battle , Sussex , England - 26 February 1963 | Bei der Ankunft am Londoner Flughafen mit der Flugbegleiterin Jean Reed sind sie auf dem Weg zum Tibetan House im British Pestalozzi Children ' s Village in Oaklands Park , Sedlescombe , Battle , Sussex , England - 26 . Februar 1963 |
| Our kaltachak most likely was once owned by a
woman from one of these first families . | Unser Kaltachak war wahrscheinlich einmal im Besitz einer Frau aus einer dieser ersten Familien . |
| Little Geraldine Figland , form Cape Town , South Africa , meets her new school mates at St Bernard ' s Convent Preparatory School in Slough , Buckinghamshire , England after being adopted by Mrs Eileen MacDougall . | Die kleine Geraldine Figland aus Kapstadt , Südafrika , trifft ihre neuen Schulkameraden an der St . Bernard ' s Convent Preparatory School in Slough , Buckinghamshire , England , nachdem sie von Frau Eileen MacDougall adoptiert wurde . |

## Music
| English | German |
|----|----|
| On the dance floor at the Sunset Club in Soho , London . | Auf der Tanzfläche im Sunset Club in Soho , London . |
| Applying the make - up . | Auftragen des Make - ups . |
| Here the ' Worcester Boys ' are messing around in the grounds of Foots Cray Place , Kent , which is their new quarters for the duration of the war . | Hier tummeln sich die Worcester Boys auf dem Gelände von Foots Cray Place , Kent , das für die Dauer des Krieges ihr neues Quartier ist . |

## Sport
| English | German |
|----|----|
| The prow is shaped according to the tradition of the area , sometimes additional designs are carved on the sides , and it may be painted with natural pigments or store house paint . | Der Bug ist nach der Tradition der Gegend geformt , manchmal werden zusätzliche Muster an den Seiten geschnitzt , und er kann mit Naturpigmenten oder Lagerhausfarbe bemalt werden . |
| Pair of men ' s golf shoes of brown leather , with shoe trees , Great Britain , 20th century . | Paar Herren - Golfschuhe aus braunem Leder , mit Schuhspanner , Großbritannien , 20. |
| It is carved from a single heavy plank . | Es ist aus einem einzigen schweren Brett geschnitzt . |
