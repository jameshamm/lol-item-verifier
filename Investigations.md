This file details some issues which need a human touch. The problems are either not straightforward to automatically find, need more information on their internals, or are minor and it is probably not worth looking into.

## Legacy Effects

### Doran's Balde (1055):

    Issue: Dblade has an effect "Effect1Amount" which is currently set to "10". This is probably the legacy code that gave it AD, but could related to the gold per 10 it used to give.

    Task: Sift through previous item set versions until this number is affected. The most likely patch this became obsolete is 3.14

### Ardent Censer (3504):

    Issue: In the patch 7.17, ardent censer had it's on hit effect changed from draining 20 - 35 health to a flat 25. In addition, it's attack speed buff has also been fixed to 25% from 20% to 35%. The item still contains "Effect6Amount" which is set to "0.35", and "Effect7Amount" at "35". These seem to no longer be in use.

## Generic Issues

### Cull (1083)
    Issue: cull has dblade listed in its colloq.

    Task: Verify the item appears when you search for dblade in the shop. Also check how long this has been the case.


### Enchantments (Many)
    Issue: There appears to be repeated enchantments in the data set.

    Task: Find any place they are different, and see if the item can be found in the online item shop.


### Total Biscuit of Rejuvenation (2010, not the other one)

    Issue: This item does not mention it's limit of 5 in it's description, whereas health potions do.

    Task: Find any other items which have a limited amount available at once, either through the stack property, or through the <groupLimit> tag in the description


### Sightstone (2045, 2049)

    Issue: Sightstone will consume a charge when a ward is placed. Is the charge unique to each sightstone?

    Task: Investigate what happens when multiple sightstones are used from a single inventory.


### Base health regen and base mana regen

    Issue: The above stats are not listed in some items stats or effects. See forbidden idol for an example.

    Task: Find all items that affect base hp and mana regen.


### Control Ward (2055)

    Issue: Searching for doran brings up the control ward.

    Task: Find the cause of this.