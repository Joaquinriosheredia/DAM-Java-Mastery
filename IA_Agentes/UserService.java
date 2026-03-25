```java
package com.crewai.service;

import com.crewai.model.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service("userService")
public class UserService implements UserDetailsService {

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // Simulate fetching the user from a database or other storage mechanism.
        return new User();  // In practice, fetch and return a real user object here.
    }
}
```