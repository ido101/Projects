using Library;
Console.WriteLine("=== INITIALIZING LIBRARY TEST ===");

            try
            {
                // 1. Create some Authors
                Author author1 = new Author("J.K.", "Rowling", new DateTime(1965, 7, 31));
                Author author2 = new Author("George", "Orwell", new DateTime(1903, 6, 25));

                // 2. Create some Books
                // Note: Make sure to add them to the BookDataBase after creation (following best practices)
                Book book1 = new Book("Harry Potter", author1, 300, "A wizard's journey", Genres.Fiction, "Bloomsbury", 14);
                Book book2 = new Book("1984", author2, 328, "Dystopian classic", Genres.ScienceFiction, "Secker & Warburg", 14);

                BookDataBase.AddBook(book1);
                BookDataBase.AddBook(book2);

                Console.WriteLine($"\nAdded books successfully! Barcodes generated:");
                Console.WriteLine($"- {book1.Title}: {book1.BarCode}");
                Console.WriteLine($"- {book2.Title}: {book2.BarCode}");

                // 3. Create Subscribers of different types
                RegularSubscriber regularSub = new RegularSubscriber("Alice", "Smith", 25);
                StudentSubscriber studentSub = new StudentSubscriber("Bob", "Johnson", 20);
                DisabledSubscriber disabledSub = new DisabledSubscriber("Charlie", "Brown", 30);
                disabledSub.IsIntellectuallyDisabled = true; // Test specific property logic

                // 4. Test Book Info before loaning
                Console.WriteLine("\n--- Testing Book Status (Before Loan) ---");
                BookDataBase.InfoAboutBook(book1.BarCode);

                // 5. Test Loaning Books (Polymorphism in action with different loan periods!)
                Console.WriteLine("\n--- Testing Book Loans ---");
                book1.LoanBook(studentSub); // Student gets double the loan period
                Console.WriteLine($"Loaned '{book1.Title}' to student {studentSub.FirstName}. Return date: {book1.ReturnDate}");

                // 6. Test Book Info after loaning
                Console.WriteLine("\n--- Testing Book Status (After Loan) ---");
                BookDataBase.InfoAboutBook(book1.BarCode);

                // 7. Test Copy Counting
                Console.WriteLine("\n--- Testing Copy Counter ---");
                BookDataBase.HowManyCopies("Harry Potter", "J.K. Rowling"); // Should be 0 available since it's lent out
                BookDataBase.HowManyCopies("1984", "George Orwell");          // Should be 1 available

                // 8. Test Returning a Book
                Console.WriteLine("\n--- Testing Book Return ---");
                book1.ReturnBook();
                Console.WriteLine($"'{book1.Title}' has been returned.");
                
                // Check status again
                BookDataBase.InfoAboutBook(book1.BarCode);

                // 9. Test Custom Exceptions
                Console.WriteLine("\n--- Testing Exception Handling ---");
                try
                {
                    // Trying to return a book that isn't loaned should throw our custom exception
                    book1.ReturnBook();
                }
                catch (BookLoaningException ex)
                {
                    Console.WriteLine($"Caught expected exception: {ex.Message}");
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }

            Console.WriteLine("\n=== TEST COMPLETED ===");