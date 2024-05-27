# There are many filesystems for storage devices in linux
# There's pre-installed one that comes with linux

# Common file systems
  #  1.) Extended file systems(ext)
     #  - Introduced with linux operating system
     #  - Unix - like filesystem
     #  - Uses virtual directories to handle physical devices.
     #  - Inodes - Used to track information about files stored in the virtual directory.
     #  - Linux references each inode in the inode table using a unique number(inode number)
     #  - Can only retain files upto 2GB in size
     #  - Stored files in data-blocks
     #  - files were written to a physical device
     #  - The blocks used to store this data tend to be scattered throughout the device
     #  - The above is called fragmentation
     #  - 

  #  2.) ext2 file systems
     #  - Expansion of capabilities of the ext filesystem
     #  - Maintains same structure as ext
     #  - Maximum file size allowed now is 2TB later verions allowed upto 32TB
     #  - Reduces Fragmentation by allocating disk blocks in groups when saving files
     #  - This was the default file system used for many years
     #  - limitations; Each time filesystem stores or updates a file it must modify inode table
     #  - If the inode table entry isn't completed when the file is stored, the file doesn't exist
  
  #  3.) Journaling filesystems
     #  - Instead of writing data directly to the storage device and then updating the inode table,
     #    Journaling filesystems write file changes to a temporary file called JOURNAL
     #  - After  data is written to storage device and inode table, journal entry is deleted.
     #  - Slowest file system

  #  4.) ext3 filesystem
     #  - Added in 2001
     #  - Same inode table as ext2 filesystem
     #  - Adds a journal file to each storage device
     #  - Uses the ordered mode of journaling, only writing the inode information to the journal file
     #  - Doesn't remove data in the inode table unless datablocks have successfully written to the storage device
     #  - Doesn't provide recovery from accidental deletion of files
     #  - No built-in data compression is available
     #  - Doesn't support encrypting files
    
  #  5.) ext4 filesystem
     #  - Added in 2008
     #  - Default filesystem in linus distributions such as UBUNTU
     #  - Supports compression and encryptions
     #  - Supports a feature called extents
     #  - Extents allocate space on a storage device in blocks.
     #  - Only stores the starting block location in the inode table
     #  - Incorporate block pre-allocation
     #  - 