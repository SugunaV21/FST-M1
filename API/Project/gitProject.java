package activities;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;
import org.testng.Assert;
import org.testng.Reporter;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.*;


public class gitProject {

        // Declare request specification
        RequestSpecification requestSpec;
        ResponseSpecification responseSpec;
        String baseURi="https://api.github.com/user/keys/KeyId";

  //  String baseURiKey="https://api.github.com/user/keys";
    int KeyId=87727847;
        @BeforeTest
        public void setUp() {
            // Create request specification
            String Request_Body = "{\"title\": TestAPIKey,\"key\":\"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINeq9Or9aHEDP3WrG1ADTQOeJWdDlH3tnO2tQGsm+z+h\"}";

            requestSpec = new RequestSpecBuilder()
                    .addHeader("Authorization","token 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")
                    .addHeader("Content-Type","application/json")
                    .setBody(Request_Body)
                    .setBasePath("https://api.github.com").build();

            responseSpec = new ResponseSpecBuilder()
                    //.expectResponseTime(3000L)
                    .expectContentType(ContentType.JSON)
                    .build();
        }

        @Test
        public void testPost() {

            Response response = given().spec(requestSpec)
                    .post();
            String keyId= response.then().extract().path("[0].id");
             // Print response
            String body = response.getBody().asPrettyString();
            System.out.println(body);
            response.then().spec(responseSpec).statusCode(201);
            // Assertion

        }
    @Test(priority=1)
    public void testGet() {

        Response response =
                given().spec(requestSpec)
                        .pathParam("KeyId",KeyId)// Use requestSpec.
                        .get("/{KeyId}");// Send GET request
        Reporter.log("get keyId of response");
        // Print response
        System.out.println(response);
        // Assertion
         response.then().spec(responseSpec).statusCode(200);

    }

    @Test(priority=2)
    public void testDelete() {

        Response response =
                given().spec(requestSpec)
                        .pathParam("KeyId",KeyId)// Use requestSpec.
                        .get("/{KeyId}");// Send GET request
        Reporter.log("Deleted keyId of response");
        // Print response
        System.out.println(response);
        // Assertion
        response.then().spec(responseSpec).statusCode(204);

    }

    }

