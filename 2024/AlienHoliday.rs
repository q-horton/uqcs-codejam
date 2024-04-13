use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'alien' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING message as parameter.
 */

fn caesar(encoded: &str, index: u8) -> String {
    let chars: Vec<char> = encoded.chars().collect::<Vec<char>>();
    let mut output: String = String::new();
    for i in chars {
        let decoded: u8;
        if (i as u8) >= 'a' as u8 && (i as u8) <= 'z' as u8 {
            decoded = (((i as u8 - 'a' as u8) + index) % 26) + ('a' as u8);
        } else if (i as u8) >= 'A' as u8 && (i as u8 <= 'Z' as u8) {
            decoded = (((i as u8 - 'A' as u8) + index) % 26) + ('A' as u8);
        } else {
            decoded = i as u8;
        }
        output.push(decoded as char);
    }
    output
}

fn alien(message: &str) -> String {
    // Write your code here
    let last_char: char = message.chars().collect::<Vec<char>>()[message.len() - 1];
    let offset: u8;
    if last_char >= 't' {
        offset = 26 - (last_char as u8 - 't' as u8);
    } else {
        offset = 't' as u8 - last_char as u8;
    }
    
    caesar(message, offset)
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let message = stdin_iterator.next().unwrap().unwrap();

    let result = alien(&message);

    writeln!(&mut fptr, "{}", result).ok();
}

