use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'char_finder' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts following parameters:
 *  1. CHARACTER c
 *  2. INTEGER n
 *  3. STRING_ARRAY r
 */

fn char_finder(c: char, n: i32, r: &[String]) -> Vec<String> {
    // Write your code here
    let mut out: Vec<String> = Vec::new();
    for i in r {
        let mut count: i32 = 0;
        for j in i.chars() {
            if j == c {
                count += 1;
            }
        }
        if count == n {
            out.push(i.clone());
        }
    }
    return out;
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let c = stdin_iterator.next().unwrap().unwrap().chars().next().unwrap();

    let n = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();
    
    stdin_iterator.next();
    
    let arr: Vec<String> = stdin_iterator.next().unwrap().unwrap().trim().split(' ').map(|x| x.to_owned()).collect::<Vec<String>>();

    let result = char_finder(c, n, &arr);

    for i in 0..result.len() {
        write!(&mut fptr, "{}", result[i]).ok();

        if i != result.len() - 1 {
            write!(&mut fptr, " ").ok();
        }
    }

    writeln!(&mut fptr).ok();
}

