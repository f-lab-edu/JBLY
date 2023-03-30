package com.flab.jbly.user;

import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
import java.util.HashMap;
import java.util.concurrent.atomic.AtomicLong;

public class HashMapRepository implements UserRepository {

    private HashMap<Long, User> inMemoryRepo = new HashMap<>();
    private AtomicLong sequence = new AtomicLong();

    public void clearDB() {
        inMemoryRepo.clear();
    }

    @Override
    public User save(User user) {
        if (user.getId() == null || user.getId() <= 0L) {
            Long userId = sequence.incrementAndGet();
            user.currentId(userId);
            inMemoryRepo.put(userId, user);
        } else {
            inMemoryRepo.put(user.getId(), user);
        }
        return user;
    }

    @Override
    public boolean existsByUserId(String userId) {
        for (User user : inMemoryRepo.values()) {
            if (user.getUserId().equals(userId)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public User findByUserId(String userId) {
        return inMemoryRepo
            .values()
            .stream()
            .filter(user -> userId.equals(user.getUserId()))
            .findFirst().orElse(null);
    }

    @Override
    public User getUserById(Long id) {
        return inMemoryRepo.get(id);
    }

    @Override
    public void deleteUserById(Long id) {
        for (User user : inMemoryRepo.values()) {
            if (user.getId() == id) {
                inMemoryRepo.remove(id);
                return;
            }
        }
        throw new IllegalArgumentException();
    }
}
