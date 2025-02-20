Below is a comprehensive tutorial with examples of Bash scripts designed to help you learn Bash scripting from beginner to advanced levels. Each example is explained and covers a specific concept or use case.

Bash Scripting Tutorial: Examples for Learning
1. Hello World
The simplest script to get started.

```bash

#!/bin/bash
# Hello World Script
echo "Hello, World!"
```
Explanation:

#!/bin/bash: Specifies the interpreter (Bash).

echo: Prints text to the terminal.

2. Variables
Learn how to declare and use variables.

```bash
#!/bin/bash
# Variables Example
name="John"
age=25
echo "My name is $name and I am $age years old."
```
Explanation:

Variables are declared without spaces around =.

Use $ to access the value of a variable.

3. User Input
Read input from the user.

```bash
#!/bin/bash
# User Input Example
echo "What is your name?"
read name
echo "Hello, $name!"
```
Explanation:

read: Captures user input and stores it in a variable.

4. Conditional Statements
Use if-else for decision-making.

```bash
#!/bin/bash
# Conditional Example
echo "Enter a number:"
read num
if [ $num -gt 10 ]; then
    echo "The number is greater than 10."
else
    echo "The number is 10 or less."
fi
```
Explanation:

if [ condition ]; then: Checks a condition.

-gt: Greater than (other operators: -lt, -eq, -ne, etc.).

fi: Ends the if block.

5. Loops
Use for and while loops.

For Loop
```bash
#!/bin/bash
# For Loop Example
for i in {1..5}; do
    echo "Iteration $i"
done
```
While Loop
```bash
#!/bin/bash
# While Loop Example
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done
```
Explanation:

for: Iterates over a range or list.

while: Repeats as long as a condition is true.

6. Functions
Create reusable code blocks.

```bash
#!/bin/bash
# Function Example
greet() {
    echo "Hello, $1!"
}
greet "Alice"
greet "Bob"
```
Explanation:

greet(): Defines a function.

$1: Refers to the first argument passed to the function.

7. Command-Line Arguments
Access arguments passed to the script.

```bash
#!/bin/bash
# Command-Line Arguments Example
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Number of arguments: $#"
```
Explanation:

$1, $2: Access specific arguments.

$@: All arguments.

$#: Number of arguments.

8. File Operations
Read and write files.

```bash
#!/bin/bash
# File Operations Example
file="example.txt"
echo "Creating $file..."
echo "Hello, File!" > $file
echo "Content of $file:"
cat $file
```
Explanation:

>: Overwrites a file.

>>: Appends to a file.

cat: Displays file content.

9. Arrays
Store and manipulate lists of items.

```bash
#!/bin/bash
# Array Example
fruits=("Apple" "Banana" "Cherry")
echo "First fruit: ${fruits[0]}"
echo "All fruits: ${fruits[@]}"
```
Explanation:

fruits=(): Declares an array.

${fruits[0]}: Accesses the first element.

${fruits[@]}: Accesses all elements.

10. Case Statements
Handle multiple conditions.

```bash
#!/bin/bash
# Case Statement Example
echo "Enter a fruit:"
read fruit
case $fruit in
    "Apple") echo "You chose Apple." ;;
    "Banana") echo "You chose Banana." ;;
    "Cherry") echo "You chose Cherry." ;;
    *) echo "Unknown fruit." ;;
esac
```
Explanation:

case: Matches a variable against patterns.

*): Default case (like else).

11. Error Handling
Check for errors and exit gracefully.

```bash
#!/bin/bash
# Error Handling Example
echo "Enter a file name:"
read file
if [ -f "$file" ]; then
    echo "File exists."
else
    echo "File does not exist. Exiting."
    exit 1
fi
```
Explanation:

-f: Checks if a file exists.

exit 1: Exits the script with an error code.

12. Debugging
Enable debugging to trace script execution.

```bash
#!/bin/bash
# Debugging Example
set -x  # Enable debugging
echo "Debugging is enabled."
set +x  # Disable debugging
echo "Debugging is disabled."
```

Explanation:

set -x: Enables debugging.

set +x: Disables debugging.

13. Subshells and Command Substitution
Run commands in subshells and capture output.

```bash
#!/bin/bash
# Subshell Example
current_date=$(date)
echo "Today's date is $current_date."
```
Explanation:

$(command): Captures the output of a command.

14. Networking
Ping a remote server.

```bash
#!/bin/bash
# Networking Example
echo "Enter a hostname or IP address:"
read host
ping -c 4 $host
```
Explanation:

ping -c 4: Sends 4 ICMP packets to the host.

15. Advanced: Process Management
List and kill processes.

```bash
#!/bin/bash
# Process Management Example
echo "Listing all running processes:"
ps aux
echo "Enter a PID to kill:"
read pid
kill -9 $pid
```
Explanation:

ps aux: Lists all processes.

kill -9: Forcefully kills a process.

16. Advanced: Cron Jobs
Schedule a script to run periodically.

```bah
#!/bin/bash
# Cron Job Example
echo "Adding a cron job to run this script every minute..."
(crontab -l 2>/dev/null; echo "* * * * * /path/to/your/script.sh") | crontab -
echo "Cron job added."
```
Explanation:

crontab -l: Lists existing cron jobs.

crontab -: Adds a new cron job.

17. Advanced: Regular Expressions
Use regex for pattern matching.

bash
Copy
#!/bin/bash
# Regex Example
echo "Enter an email address:"
read email
if [[ $email =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$ ]]; then
    echo "Valid email."
else
    echo "Invalid email."
fi
Explanation:

=~: Matches a string against a regex pattern.

18. Advanced: Working with APIs
Fetch data from an API.

bash
Copy
#!/bin/bash
# API Example
echo "Fetching data from an API..."
response=$(curl -s https://api.github.com/users/octocat)
echo "GitHub user data:"
echo $response | jq .
Explanation:

curl -s: Fetches data silently.

jq: Parses JSON output.

19. Advanced: Backup Script
Create a backup of a directory.

bash
Copy
#!/bin/bash
# Backup Script Example
backup_dir="/backup"
source_dir="/home/user/documents"
timestamp=$(date +"%Y%m%d%H%M%S")
backup_file="$backup_dir/backup_$timestamp.tar.gz"
tar -czf $backup_file $source_dir
echo "Backup created at $backup_file."
Explanation:

tar -czf: Compresses and archives files.

20. Advanced: Password Generator
Generate a random password.

bash
Copy
#!/bin/bash
# Password Generator Example
password=$(openssl rand -base64 12)
echo "Generated password: $password"
Explanation:

openssl rand -base64: Generates random data.

Conclusion
These examples cover a wide range of Bash scripting concepts, from basic to advanced. Practice each example, modify them, and experiment to deepen your understanding. Bash scripting is a powerful skill for automating tasks and managing systems. Happy scripting! 🚀
