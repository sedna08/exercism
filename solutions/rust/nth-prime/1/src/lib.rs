fn is_prime(n: u32) -> bool {
    let mut i = 5;
    while i <= n / i {
        if n % i == 0 || n % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }

    true
}

pub fn nth(n: u32) -> u32 {
    match n {
        0 => return 2,
        1 => return 3,
        _ => {}
    }

    let mut count = 1;
    let mut candidate = 5;
    let mut step = 2;

    loop {
        if is_prime(candidate) {
            count += 1;
            if count == n {
                return candidate;
            }
        }

        candidate += step;
        step = 6 - step;
    }
}