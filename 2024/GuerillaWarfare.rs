use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'decrypt' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING encrypted_string as parameter.
 */

fn decrypt(encrypted_string: &str) -> String {
    // Write your code here
    let key_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let key_arr = key_str.chars().collect::<Vec<char>>();
    
    let encrypted: Vec<String> = encrypted_string.trim().split(' ').map(|x| x.to_owned()).collect::<Vec<String>>();
    let mut decrypted: String = String::new();
    
    for i in encrypted {
        let letters = i.chars().collect::<Vec<char>>();
        let mut val: u8 = 0;
        for j in letters {
            for k in 0..key_arr.len() {
                if key_arr[k] == j {
                    val += k as u8 + 1;
                }
            }
        }
        decrypted.push(val as char);
    }
    
    decrypted
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let encrypted_string = stdin_iterator.next().unwrap().unwrap();

    let result = decrypt(&encrypted_string);

    writeln!(&mut fptr, "{}", result).ok();
}

