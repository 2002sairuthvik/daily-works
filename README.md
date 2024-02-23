
linux -  Account Management 
 /etc/passwd # => users and info
 /etc/shadow # => users' passwords
 /etc/group # => groups 

creating a user account - useradd [OPTIONS] username
OPTIONS:
 -m => create home directory
 -d directory => specify another home directory
 -c "comment"
 -s shell
-G => specify the secondary groups (must exist)
-g => specify the primary group (must exist)

changing a user account  - usermod [OPTIONS] username

 deleting a user account - userdel -r username # => -r removes user's home directory as well
 creating a group  - groupadd group_name
 deleting a group -groupdel group_name
 displaying all groups -cat /etc/groups
 displaying the groups a user belongs to - groups
 creating admin users : add the user to sudo group in Ubuntu and wheel group in CentOS - ---:usermod -aG sudo john

who -H # => displays logged in users
id # => displays the current user and its groups
whoami # => displays EUID
 
listing who’s logged in and what’s their current process. -:w  , uptime
printing information about the logins and logouts of the users - last   , last -u username


File Permissions 
chmod 
u = User
g = Group
o = Others/World
a = all 
r = Read
w = write
x = execute
- = no access
 
displaying the permissions (ls and stat)
ls -l /etc/passwd
stat /etc/shadow
changing the permissions using the relative (symbolic) mode
chmod u+r filename
chmod u+r,g-wx,o-rwx filename
chmod ug+rwx,o-wx filename
chmod ugo+x filename
chmod a+r,a-wx filename
 
changing the permissions using the absolute (octal) mode
PERMISSIONS      EXAMPLE
u   g   o
rwx rwx rwx     chmod 777 filename
rwx rwx r-x     chmod 775 filename
rwx r-x r-x     chmod 755 filename
rwx r-x ---     chmod 750 filename
rw- rw- r--     chmod 664 filename
rw- r-- r--     chmod 644 filename
rw- r-- ---     chmod 640 filename
 
setting the permissions as of a reference file
chmod --reference=file1 file2
 
changing permissions recursively
chmod -R u+rw,o-rwx filename
 
SUID (Set User ID)
 
displaying the SUID permission
ls -l /usr/bin/umount 
 stat /usr/bin/umount 
   
 setting SUID
chmod u+s executable_file
chmod 4XXX executable_file      # => Ex: chmod 4755 script.sh
 
 
SGID (Set Group ID)
displaying the SGID permission
ls -ld projects/
stat projects/
 
setting SGID
chmod 2750 projects/
chmod g+s projects/
  
The Sticky Bit 
 
displaying the sticky bit permission
ls -ld /tmp/
stat /tmp/

 
setting the sticky bit
mkdir temp
chmod 1777 temp/
chmod o+t temp/
ls -ld temp/
 
 
 UMASK
displaying the UMASK
umask 
 
setting a new umask value
umask new_value     # => Ex: umask 0022
 
Changing File Ownership (root only)
 
changing the owner
chown new_owner file/directory      # => Ex: sudo chown john a.txt
 
changing the group owner
chgrp new_group file/directory
 
changing both the owner and the group owner
chown new_owner:new_group file/directory
 
changing recursively the owner or the group owner
chown -R new-owner file/directory
 
displaying the file attributes
lsattr filename
 
changing the file attributes
chattr +-attribute filename     # => Ex: sudo chattr +i report.txt