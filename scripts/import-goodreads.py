import csv, json
from pathlib import Path

src = Path("imports/goodreads_library_export.csv")
out = Path("src/data/books.json")

books = []
with src.open(newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row.get("Title", "").strip()
        if not title:
            continue

        book_id = row.get("Book Id", "").strip()
        isbn13 = row.get("ISBN13", "").strip()
        year = row.get("Year Published", "").strip()

        books.append({
            "title": title,
            "status": "published",
            "category": "Published Works",
            "authorsDisplayed": "Clark Aurelian Flameprint ∮ Marci Ramona Wojcik",
            "publisher": row.get("Publisher", "").strip() or "TBD",
            "isbn13": isbn13 or "TBD",
            "asin": "TBD",
            "binding": row.get("Binding", "").strip(),
            "pages": row.get("Number of Pages", "").strip(),
            "yearPublished": year,
            "source": "Goodreads export / KDP-Bowker normalization pending",
            "goodreadsUrl": f"https://www.goodreads.com/book/show/{book_id}" if book_id else "",
            "description": "Published work in the Clark∮Marci / CFRM corpus. Description pending normalization."
        })

out.write_text(json.dumps(books, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {len(books)} records to {out}")
