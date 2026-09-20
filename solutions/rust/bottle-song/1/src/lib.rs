fn match_num_word(num: u32) -> &'static str {
    match num {
        10 => "Ten",
        9 => "Nine",
        8 => "Eight",
        7 => "Seven",
        6 => "Six",
        5 => "Five",
        4 => "Four",
        3 => "Three",
        2 => "Two",
        1 => "One",
        0 => "No",
        _ => "Many", 
    }
}

fn pluralize(num: u32) -> &'static str {
    if num == 1 { "bottle" } else { "bottles" }
}

fn verse(n: u32) -> String {
    format!(
        "{0} green {1} hanging on the wall,\n\
         {0} green {1} hanging on the wall,\n\
         And if one green bottle should accidentally fall,\n\
         There'll be {2} green {3} hanging on the wall.\n",
        match_num_word(n),
        pluralize(n),
        match_num_word(n - 1).to_lowercase(), // Makes "No" lowercase mid-sentence
        pluralize(n - 1)
    )
}

pub fn recite(start_bottles: u32, take_down: u32) -> String {
    let mut result: String = String::new();

    for i in 0..take_down {
        let current: u32 = start_bottles - i;
        
        result.push_str(&verse(current));
        
        if i < take_down - 1 {
            result.push('\n');
        }
    }
    
    result
}