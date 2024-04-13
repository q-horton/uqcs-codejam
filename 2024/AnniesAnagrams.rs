use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};
use std::collections::HashMap;

/*
 * Complete the 'test_if_anagrams' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER array_length
 *  2. STRING_ARRAY anagram_array
 */

fn chars_to_map(chars: Vec<char>) -> HashMap<char, i32> {
    let mut output: HashMap<char, i32> = HashMap::new();
    for i in chars {
        let val: char;
        if i.is_uppercase() {
            val = ((i as u8) + ('a' as u8 - 'A' as u8)) as char;
        } else {
            val = i;
        }
        
        if output.contains_key(&val) {
            output.insert(val, output[&val] + 1);
        } else {
            output.insert(val, 1);
        }
    }
    output
}

fn test_if_anagrams(array_length: i32, anagram_array: &[String]) -> i32 {
    // Write your code here
    let first: Vec<char> = anagram_array[0].chars().collect::<Vec<char>>();
    let first_map: HashMap<char, i32> = chars_to_map(first);
    for i in anagram_array {
        let chars: Vec<char> = i.chars().collect::<Vec<char>>();
        let cmap: HashMap<char, i32> = chars_to_map(chars);
        for j in cmap.keys() {
            if !first_map.contains_key(&j) {
                return 0;
            }
            if cmap[&j] != first_map[&j] {
                return 0;
            }
        }
    }
    1
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let length = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let mut ana_array: Vec<String> = Vec::with_capacity(length as usize);

    for _ in 0..length {
        let ana_array_item = stdin_iterator.next().unwrap().unwrap();
        ana_array.push(ana_array_item);
    }

    let result = test_if_anagrams(length, &ana_array);

    writeln!(&mut fptr, "{}", result).ok();
}

