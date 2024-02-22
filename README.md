Facing power issues at home sir , i will report my learnings :
linux -  Account Management 
 /etc/passwd # => users and info
 /etc/shadow # => users' passwords
 /etc/group # => groups -
creating a user account - useradd [OPTIONS] username
OPTIONS:
 -m => create home directory
 -d directory => specify another home directory
 -c "comment"
# -s shell
# -G => specify the secondary groups (must exist)
# -g => specify the primary group (must exist)

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