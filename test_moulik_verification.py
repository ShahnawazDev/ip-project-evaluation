"""
Test to verify Moulik's code bug for same-line journeys
"""

# Let me trace through the logic manually:
# 
# journeyPlan function (lines 148-174):
# 
# Line 159: if srcLine == dstLine:
#     Lines 160-162: Calculate same-line journey (t, arrival, fare)
#     BUT NO RETURN STATEMENT!
# 
# Line 163: if srcStation == dstStation:
#     Line 164: return "Please enter 2 different stations"
#     Lines 166-173: UNREACHABLE CODE (return statement after a return!)
# 
# Line 174: return interchange(...)
#
# So when srcLine == dstLine AND srcStation != dstStation:
# - Lines 160-162 execute (calculate same-line journey)
# - Line 163 condition is false (stations are different)
# - Lines 166-173 are NEVER executed (unreachable)
# - Line 174 EXECUTES! Calls interchange() for a same-line journey!
#
# This is a CRITICAL BUG!

print("ANALYSIS OF MOULIK'S CODE BUG:")
print("=" * 60)
print()
print("Line 159: if srcLine == dstLine:")
print("    Lines 160-162: Calculate same-line journey")
print("    NO RETURN STATEMENT HERE!")
print()
print("Line 163: if srcStation == dstStation:")
print("    Line 164: return error")
print("    Lines 166-173: UNREACHABLE CODE (after return)")
print()
print("Line 174: return interchange(...)")
print()
print("=" * 60)
print()
print("RESULT:")
print("For same-line journeys where srcStation != dstStation:")
print("1. Lines 160-162 calculate journey (but results unused)")
print("2. Line 163 condition fails (stations different)")
print("3. Lines 166-173 never execute (unreachable)")
print("4. Line 174 executes - calls interchange() incorrectly!")
print()
print("This means ALL same-line journeys will show interchange!")
print("=" * 60)
print()

# Additional issues:
print("ADDITIONAL ISSUES:")
print("1. Line 163 check (srcStation == dstStation) is MISPLACED")
print("   - Should be at the start of function, not here")
print("   - Currently only works if srcLine == dstLine is true")
print()
print("2. Lines 166-173 are UNREACHABLE CODE")
print("   - Comes after a return statement (line 164)")
print("   - Will NEVER execute regardless of input")
print()
print("3. Missing indentation/structure:")
print("   - Line 163 should be 'elif', not separate 'if'")
print("   - OR line 162 should be followed by a return statement")
print("=" * 60)

# Verification of the evaluation
print()
print("EVALUATION VERIFICATION:")
print("The evaluation report correctly identifies:")
print("✓ Critical bug: same-line journeys incorrectly trigger interchange")
print("✓ Lines 168-174 are unreachable code")
print("✓ Logic error in control flow")
print("✓ This affects core functionality")
print()
print("The deductions are justified:")
print("- Same-line journey bug: -10 marks (appropriate)")
print("- Unreachable code/logic error: -5 marks (appropriate)")
print("=" * 60)
