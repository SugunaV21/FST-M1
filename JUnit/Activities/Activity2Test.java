package Activity;
import Activities.BankAccount;
import Activities.NotEnoughFundsException;
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

public class Activity2Test {



        @Test
        void notEnoughFunds() {
            // Create an object for BankAccount class
            BankAccount account = new BankAccount(9);

            // Assertion for exception
            assertThrows(NotEnoughFundsException.class, () -> account.withdraw(10),
                    "Balance must be greater than amount of withdrawal");
            //System.out.println("Not Enough balance");
        }

        @Test
        void enoughFunds() {
            // Create an object for BankAccount class
            BankAccount account = new BankAccount(100);

            // Assertion for no exceptions
            assertDoesNotThrow(() -> account.withdraw(100));
            //System.out.println("Enough balance");
        }
    }

