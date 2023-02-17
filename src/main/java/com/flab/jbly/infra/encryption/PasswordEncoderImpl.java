package com.flab.jbly.infra.encryption;

import com.flab.jbly.domain.user.PasswordEncoder;
import com.flab.jbly.infra.exception.ErrorCode;
import com.flab.jbly.infra.exception.user.EncoderNoSuchAlgorithmException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import org.springframework.stereotype.Component;

@Component
public class PasswordEncoderImpl implements PasswordEncoder {

    @Override
    public String encrypt(String password) {

        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(password.getBytes());
            return bytesToHex(md.digest());
        } catch (NoSuchAlgorithmException e) {
            throw new EncoderNoSuchAlgorithmException("EncoderNoSuchAlgorithmException", ErrorCode.ENCODER_FAILED_ERROR);
        }
    }
    public static String bytesToHex(byte[] bytes) {
        StringBuilder builder = new StringBuilder();
        for (byte b: bytes) {
            builder.append(String.format("%02x", b));
        }
        return builder.toString();
    }

    @Override
    public boolean matches(String rawSt, String encodedSt) {
        return this.encrypt(rawSt).equals(encodedSt);
    }
}