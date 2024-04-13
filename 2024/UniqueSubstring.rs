use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};
use std::collections::HashSet;

/*
 * Complete the 'unique_substring' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING s
 */

fn unique_substring(n: i32, s: &str) -> String {
    // Write your code here
    for i in 0..(s.len() - n as usize) {
        let mut seen: HashSet<char> = HashSet::new();
        let mut early_break: bool = false;
        for j in &s.chars().collect::<Vec<char>>()[i..i+n as usize] {
            if seen.contains(j) {
                early_break = true;
                break;
            } else {
                seen.insert(*j);
            }
        }
        if !early_break {
            return s.chars().collect::<Vec<char>>()[i..i+n as usize].iter().collect::<String>();
        }
    }
    "".to_owned()
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let nn = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let ss = stdin_iterator.next().unwrap().unwrap();

    let yy = unique_substring(nn, &ss);

    writeln!(&mut fptr, "{}", yy).ok();
}

