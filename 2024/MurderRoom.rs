use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'survivor' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */

fn survivor(n: i32) -> i32 {
    // Write your code here
    let mut line: Vec<bool> = Vec::new();
    for _ in 0..n {
        line.push(true);
    }
    let mut index: usize = 0;
    let mut count: i32 = n;
    let mut kill_mode: bool = false;
    
    while count > 1 {
        if line[index] {
            if kill_mode {
                line[index] = false;
                count -= 1;
            }
            kill_mode ^= true;
        }
        index = (index + 1) % (n as usize);
    }
    
    for i in 0..line.len() {
        if line[i] {
            return i as i32 + 1;
        }
    }
    0
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    // Write your code here

    let n = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let result = survivor(n);

    writeln!(&mut fptr, "{}", result).ok();
}

