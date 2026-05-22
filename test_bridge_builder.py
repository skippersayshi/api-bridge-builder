"""Quick test run for API Bridge Builder."""
import os, json
from bridge_builder import MappingIntent, BridgeResult, ConnectionTester, KnowledgeBase

def test_connection_tester():
    tester = ConnectionTester()
    good = BridgeResult(success=True, mapping_applied={"customer_id": "cust_id", "email": "email_address"}, test_passed=False)
    assert tester.test(good) == True

    bad = BridgeResult(success=True, mapping_applied={}, test_passed=False)
    assert tester.test(bad) == False
    print("  ConnectionTester: PASS")

def test_knowledge_base():
    kb = KnowledgeBase(db_path=":memory:")
    intent = MappingIntent(source_system="Salesforce", target_system="SAP", data_fields=["email"], protocol="REST")
    result = BridgeResult(success=True, mapping_applied={"email": "email_addr"}, test_passed=True, notes="test")

    assert kb.lookup(intent) is None
    kb.store(intent, result)
    found = kb.lookup(intent)
    assert found is not None
    assert found.mapping_applied == {"email": "email_addr"}
    print("  KnowledgeBase store/lookup: PASS")

if __name__ == "__main__":
    print("Running tests...")
    test_connection_tester()
    test_knowledge_base()
    if os.getenv("ANTHROPIC_API_KEY"):
        from bridge_builder import RalphLoop
        print("  Running RalphLoop (requires API key)...")
        loop = RalphLoop()
        result = loop.run("Connect HubSpot to Stripe via REST. Map customer_id and email.")
        assert result.success
        print("  RalphLoop.run: PASS")
    else:
        print("  RalphLoop: SKIPPED (set ANTHROPIC_API_KEY to run)")
    print("All tests passed.")
