package com.capitalone.prep;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * System Design Q5: Peer-to-Peer Payment Double-Entry Ledger
 * Java Solution
 */
public class PeerToPeerLedger {

    private final Connection connection;

    public PeerToPeerLedger(Connection connection) {
        this.connection = connection;
    }

    public boolean transferFunds(String txId, String senderAcc, String receiverAcc, double amount) throws SQLException {
        connection.setAutoCommit(false);
        try {
            // Check balance with SELECT FOR UPDATE
            try (PreparedStatement checkStmt = connection.prepareStatement(
                    "SELECT balance FROM accounts WHERE account_id = ? FOR UPDATE")) {
                checkStmt.setString(1, senderAcc);
                try (ResultSet rs = checkStmt.executeQuery()) {
                    if (!rs.next() || rs.getDouble("balance") < amount) {
                        connection.rollback();
                        return false;
                    }
                }
            }

            // Insert immutable double-entry ledger rows
            String sql = "INSERT INTO ledger_entries (entry_id, transaction_id, account_id, amount, currency, entry_type) " +
                         "VALUES (gen_random_uuid(), ?, ?, ?, 'USD', 'DEBIT'), (gen_random_uuid(), ?, ?, ?, 'USD', 'CREDIT')";
            try (PreparedStatement insertStmt = connection.prepareStatement(sql)) {
                insertStmt.setString(1, txId);
                insertStmt.setString(2, senderAcc);
                insertStmt.setDouble(3, -amount);
                insertStmt.setString(4, txId);
                insertStmt.setString(5, receiverAcc);
                insertStmt.setDouble(6, amount);
                insertStmt.executeUpdate();
            }

            connection.commit();
            return true;
        } catch (Exception e) {
            connection.rollback();
            throw e;
        } finally {
            connection.setAutoCommit(true);
        }
    }
}
