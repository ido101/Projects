namespace Library
{  
    enum Genres
    {
        Fiction,
        Mystery,
        Romance,
        Biography,
        History,
        ScienceFiction
    }
    class Book
    {
        #region Fields
        public readonly string BarCode;
        static readonly Random rnd = new Random();
        private string title;
        private Author author;
        private int numOfPages;
        private string description;
        private Genres genre;
        private string publisher;
        private DateTime lendingDate;
        private DateTime returnDate;
        private bool isLent;
        private LibrarySubscriber currentBorrower;

        #endregion

        #region Properties
        public string Title
        {
            get { return title; }
            set { title = value; }
        }
        public Author Author
        {
            get { return author; }
            set { author = value; }
        }
        public int NumOfPages
        {
            get { return numOfPages; }
            set { numOfPages = value; }
        }
        public string Description
        {
            get { return description; }
            set { description = value; }
        }
        public Genres Genre
        {
            get { return genre; }
            set { genre = value; }
        }
        public string Publisher
        {
            get { return publisher; }
            set { publisher = value; }
        }
        public DateTime LendingDate
        {
            get {if(isLent) return lendingDate; else throw new BookLoaningException("Book is not loaned!");}
            set { lendingDate = value; }
        }
        public DateTime ReturnDate
        {
            get {if(isLent) return returnDate; else throw new BookLoaningException("Book is not loaned!");}
            set { returnDate = value; }
        }
        public bool IsLent
        {
            get { return isLent; }
            set { isLent = value; }
        }
        public LibrarySubscriber CurrentBorrower
        {
            get {if(IsLent) return currentBorrower; else throw new BookLoaningException("Book is not loaned!");}
            set {currentBorrower = value;}
        }
        #endregion

        #region Methods
        public Book(string title, Author author, int numOfPages, string description, Genres genre, string publisher, int lendingPeriod)
        {
            Title = title;
            Author = author;
            NumOfPages = numOfPages;
            Description = description;
            Genre = genre;
            Publisher = publisher;
            IsLent = false;
            BarCode = GenerateBarCode();
        }
        
        public void LoanBook(LibrarySubscriber borrower)
        {
            if(IsLent)
                throw new BookLoaningException("Book is already loaned.");
            CurrentBorrower = borrower;
            IsLent = true;
            LendingDate = DateTime.Now;
            ReturnDate = DateTime.Now.AddDays(borrower.LoanPeriodDays);
            borrower.LoanedBooks.Add(this);
        }
        
        public void ReturnBook()
        {
            if(!IsLent)
                throw new BookLoaningException("Book is not loaned");
            if(DateTime.Now > ReturnDate)
                CurrentBorrower.FineCollected += CurrentBorrower.PenaltyRate + (int)Genre;
            CurrentBorrower.LoanedBooks.Remove(this);
            CurrentBorrower = null;
            IsLent = false;
        }
        
        public override string ToString()
        {
            string res = $"Book title: {Title}\nAuthor: {Author}\nPages: {NumOfPages}\nShort Description: {Description}\nGenre: {Genre}\nPublisher: {Publisher}\n";
            if(IsLent)
                res += $"Loan date: {LendingDate}\nReturn date: {ReturnDate}";
            return res;
        }
        
        public string GenerateBarCode()
        {
            string res;
            while(true)
            {
                res = "";
                res += rnd.Next(100000, 999999).ToString();
                if (BookDataBase.AvailableBarCode(res))
                    break;
            }
            return res;
        }

        #endregion
    }
    static class BookDataBase
    {
        #region Fields
        private static Dictionary<string, Book> dataBase = new Dictionary<string, Book>();

        #endregion

        #region Properties
        public static Dictionary<string, Book> DataBase
        {
            get{return dataBase;} 
        }

        #endregion
        
        #region Methods
        public static void AddBook(Book book)
        {
            dataBase.Add(book.BarCode, book);
        }
        public static void AddBooks(IList<Book> books)
        {
            foreach(Book b in books)
            {
                AddBook(b);
            }
        }
        public static void RemoveBook(string code)
        {
            bool found = dataBase.Remove(code);
            if(!found){ Console.WriteLine("Book is not registered."); }
        }
        public static void HowManyCopies(string title, string author)
        {
            int count = 0;
            foreach(string key in DataBase.Keys)
            {
                if(DataBase[key].Author.ToString() == author && DataBase[key].Title == title && !DataBase[key].IsLent)
                {
                    count++;
                }
            }
            Console.WriteLine($"There are currently {count} copies available of the book {title} by {author}");
        }
        public static bool AvailableBarCode(string code)
        {
            foreach(string barCode in DataBase.Keys)
            {
                if(code == barCode)
                    return false;
            }
            return true;
        }
        public static bool InfoAboutBook(string code)
        {
            if (dataBase.TryGetValue(code, out Book book))
            {
                //Could also use ContainsKey

                if (book.IsLent)
                {
                    Console.WriteLine(book.CurrentBorrower.ToString());
                    int days = (book.ReturnDate - DateTime.Now).Days;
                    Console.WriteLine(days);
                }
                else
                {
                    Console.WriteLine("In the library.");
                }
        
                return true; // Found!
            }

            return false; // Not found
        }
        #endregion
    }
    class Author
    {
        #region Fields
        private string firstName;
        private string lastName;
        private DateTime birthDate;

        #endregion

        #region Properties
        public string FirstName
        {
            get{return firstName;}
            set{firstName = value;}
        }
        public string LastName
        {
            get{return lastName;}
            set{lastName = value;}
        }
        public DateTime BirthDate
        {
            get{return birthDate;}
            set{birthDate = value;}
        }
        #endregion

        #region Methods
        public Author(string firstName, string lastName, DateTime birthDate)
        {
            FirstName = firstName;
            LastName = lastName;
            BirthDate = birthDate;
        }
        public override bool Equals(object? obj)
        {
            return base.Equals(obj);
        }
        public override int GetHashCode()
        {
            return base.GetHashCode();
        }
        public override string ToString()
        {
            return $"{FirstName} {LastName}";
        }
        #endregion
    }
    abstract class LibrarySubscriber
    {
        #region Fields
        static List<LibrarySubscriber> Subscribers = new List<LibrarySubscriber>();
        static Random rnd = new Random();
        private double penaltyRate;
        private int loanPeriodDays;
        public readonly string subscriberId;
        private string firstName, lastName;
        private int age;
        private List<Book> loanedBooks;
        private double fineCollected;
        #endregion

        #region Properties

        public virtual double PenaltyRate
        {
            get {return 4.33;}
        }
        public virtual int LoanPeriodDays
        {
            get{return 14;}
        }
        public string FirstName
        {
            get {return firstName;}
            set {firstName = value;}
        }
        public string LastName
        {
            get {return lastName;}
            set {lastName = value;}
        }
        public int Age
        {
            get {return age;}
            set {age = value;}
        }
        public List<Book> LoanedBooks
        {
            get {return loanedBooks;}
            set {loanedBooks = value;}
        }
        public double FineCollected
        {
            get {return fineCollected;}
            set {fineCollected = value;}
        }
        #endregion

        #region Methods
        protected LibrarySubscriber(string firstName, string lastName, int age)
        {
            FirstName = firstName;
            LastName = lastName;
            Age = age;
            FineCollected = 0;
            LoanedBooks = new List<Book>();
            subscriberId = GenerateSubscriberId();
            Subscribers.Add(this);
        }

        public string GenerateSubscriberId()
        {
            string res;
            bool exists = false;
            while (true)
            {
                res = rnd.Next(100000, 999999).ToString();
                foreach(LibrarySubscriber sub in Subscribers)
                {
                    if(res == sub.subscriberId)
                        exists = true;
                        break;
                }
                if(!exists)
                    break;
            }
            return res;
        }

        public override string ToString()
        {
            return $"Subscriber ID: {subscriberId}\nName: {FirstName}, {LastName}\nAge: {age}\nFine Collected: {FineCollected}";
        }

        public void PrintAllBooks()
        {
            foreach(Book book in LoanedBooks)
            {
                Console.WriteLine(book.ToString());
            }
        }

        #endregion
    }
    class RegularSubscriber : LibrarySubscriber
    {
        #region Properties
        public override double PenaltyRate
        {
            get{return base.PenaltyRate + 3.21;}
        }
        #endregion
        
        #region Methods
        public RegularSubscriber(string firstName, string lastName, int age) : base(firstName, lastName, age){}
        #endregion
    }
    class StudentSubscriber : LibrarySubscriber
    {
        public override int LoanPeriodDays
        {
            get{return base.LoanPeriodDays*2;}
        }
        public StudentSubscriber(string firstName, string lastName, int age) : base(firstName, lastName, age){}
    }
    class DisabledSubscriber : LibrarySubscriber
    {
        #region Fields
        private bool isIntellectuallyDisabled;

        #endregion

        #region Properties
        public bool IsIntellectuallyDisabled
        {
            get{return isIntellectuallyDisabled;}
            set{isIntellectuallyDisabled = value;}
        }
        public override double PenaltyRate
        {
            get{if(IsIntellectuallyDisabled) return 0; else return base.PenaltyRate;}
        }
        public override int LoanPeriodDays
        {
            get{if(IsIntellectuallyDisabled) return base.LoanPeriodDays*3; else return base.LoanPeriodDays+30;}
        }
        
        #endregion
        
        #region Methods
        public DisabledSubscriber(string firstName, string lastName, int age) : base(firstName, lastName, age){}
        
        #endregion
    }
    class BookLoaningException : Exception
    {
        public BookLoaningException() : base() {}
        public BookLoaningException(string message) : base(message) {}
    }
}