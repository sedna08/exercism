use time::PrimitiveDateTime as DateTime;
use time::OffsetDateTime;

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    let start_sec: i64 = start.assume_utc().unix_timestamp();
    let new_seconds = start_sec + 1_000_000_000;
    let new_utc = OffsetDateTime::from_unix_timestamp(new_seconds).unwrap();
    let final_datetime = DateTime::new(new_utc.date(), new_utc.time());
    final_datetime
}
