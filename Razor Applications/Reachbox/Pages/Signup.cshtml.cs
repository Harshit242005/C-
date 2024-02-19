using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Reachbox.Pages;


#pragma warning disable CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
public class SignupModel(ApplicationDbContext context) : PageModel
#pragma warning restore CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
{
    public string Email {get; set ;}
    public string Password {get; set;}
    private readonly ApplicationDbContext _context = context;

    


    public void OnPost()
    {
        // Perform signup logic using the _context instance
        var newUser = new User
        {
            Email = Email,
            Password = Password,
            CreatedAt = DateTime.Now
        };

        _context.Users.Add(newUser);
        _context.SaveChanges();

        // Redirect to another page or perform additional actions
        // For example, you might redirect to a login page or dashboard
        RedirectToPage("/Login");
    }

    public void OnGet()
    {

    }
}