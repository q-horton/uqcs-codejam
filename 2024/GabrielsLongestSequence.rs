use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};
use std::collections::HashSet;
use std::cmp;

/*
 * Complete the 'GabesSequenceFinder' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING details
 *  2. STRING sequence
 */

fn GabesSequenceFinder(details: &str, sequence: &str) -> i32 {
    // Write your code here
    let _tot_count: i32 = details.trim().parse::<i32>().unwrap();
    let seq: Vec<i32> = sequence.trim().split(' ').map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    
    let mut unique: HashSet<i32> = HashSet::new();
    for i in seq {
        unique.insert(i);
    }
    unique.len() as i32
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let details = stdin_iterator.next().unwrap().unwrap();

    let sequence = stdin_iterator.next().unwrap().unwrap();

    let result = GabesSequenceFinder(&details, &sequence);

    writeln!(&mut fptr, "{}", result).ok();
}

