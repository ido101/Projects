class Address
{
    public string Country { get; set; }
    public string City { get; set; }
    public int HouseNum { get; set; }
    public int Floor { get; set; }
    public int Apartment { get; set; }
    public bool IsPrivate { get; set; }

    public Address(string country, string city, int houseNum, int floor, int apartment, bool isPrivate)
    {
        Country = country;
        City = city;
        HouseNum = houseNum;
        Floor = floor;
        Apartment = apartment;
        IsPrivate = isPrivate;
        if (IsPrivate)
        {
            Floor = 0;
            Apartment = 0;
        }
    }

    public Address(string country, string city, int houseNum, bool isPrivate)
    {
        Country = country;
        City = city;
        HouseNum = houseNum;
        IsPrivate = isPrivate;
        Floor = 0;
        Apartment = 0;
    }
}
class Client
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Id { get; set; }
    public Address ClientAddress { get; set; }

    public Client(string firstName, string lastName, string id, Address address)
    {
        FirstName = firstName;
        LastName = lastName;
        Id = id;
        ClientAddress = address;
    }
}
class Parcel
{
    public string ParcelProduct { get; set; }
    public double Volume { get; set; }
    public Address SourceAddress { get; set; }
    public Client Receiver { get; set; }

    public Parcel(string parcelProduct, double volume, Address sourceAddress, Client receiver)
    {
        ParcelProduct = parcelProduct;
        Volume = volume;
        SourceAddress = sourceAddress;
        Receiver = receiver;
    }
}
