# Improve Item Search

Currently the shop has a search feature. The data may show that it is not used very often, and thus should be made as lightweight as possible. However, I am interested in investigating string matching algorithms for search 'engines'.

The steps to implementing a better search mechanism are as follows:

1. Define the data and what should be important to search for. Should a hyphen "-" match items with a hyphen in them, or should it be ignored as a noisy symbol? What about space " ".
2. How are matches measured? Is it by number of corresponding characters? Is the order of the symbols important? Should all search terms be measured by the same metric, ie does "AP" mean "cap" or is it close enough to "ability power" to match? What about "PA"?
3. Determine some way of validating the search algorithm. Predefined results (this term should match these items)? All returned results should have some amount of "similarity" (wards with wards and sightstone)?
