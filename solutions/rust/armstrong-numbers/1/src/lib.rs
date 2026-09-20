pub fn is_armstrong_number(num: u32) -> bool {
    let digits = if num == 0 { 1 } else { num.ilog10() + 1 };
    let mut sum: u64 = 0;
    let mut temp: u32 = num;
    while temp > 0 {
        let digit = (temp % 10) as u64;
        sum += digit.pow(digits);
        temp /= 10;
    }
    sum == num as u64
}
