package fulchou_2.config;

import fulchou_2.Dao.User;
import fulchou_2.Service.UserService;
import fulchou_2.Service.UserServiceImp;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;


@Configuration
@ComponentScan("fulchou_2")
public class Config {
    @Bean
    User user(){
        return new User();
    }
    @Bean
    UserService userService(){
        return userServiceImp();
    }
    @Bean
    UserServiceImp userServiceImp(){
        return new UserServiceImp();
    }
}
